import mysql.connector
import sys
import getopt
import sys
import argparse
import configparser
import re

# db1 / host1 = source, db2 / host2 = destination
parser = argparse.ArgumentParser()
parser.add_argument("-db1", "--database1", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-db2", "--database2", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host1", "--host1", help = "Host choices: aws, localhost", required=True)
parser.add_argument("-host2", "--host2", help = "Host choices: aws, localhost", required=True)
parser.add_argument("-table", "--table", help = "Enter table name to sync", required=True)
parser.add_argument("-id", "--id", help = "Enter unique identifier column", required=True)
parser.add_argument("-noCE", "--no_Current_Event", help = "Enter 'true' if eventID is not in table", required=False)
args = parser.parse_args()
input_db1 = args.database1
input_host1 = args.host1
input_db2 = args.database2
input_host2 = args.host2
tableName = args.table
uniqueID = args.id
noCE = args.no_Current_Event

# Read the configuration file
config = configparser.ConfigParser()
config.read('helpers/config.ini')

# Get the database login information from the configuration (ini) file
host1 = config[input_host1 + "-" + input_db1]['host']
user1 = config[input_host1 + "-" + input_db1]['user']
passwd1 = config[input_host1 + "-" + input_db1]['passwd']
database1 = config[input_host1 + "-" + input_db1]['database']
host2 = config[input_host2 + "-" + input_db2]['host']
user2 = config[input_host2 + "-" + input_db2]['user']
passwd2 = config[input_host2 + "-" + input_db2]['passwd']
database2 = config[input_host2 + "-" + input_db2]['database']

conn1 = mysql.connector.connect(user=user1, passwd=passwd1, host=host1, database=database1)
cursor1 = conn1.cursor()
conn2 = mysql.connector.connect(user=user2, passwd=passwd2, host=host2, database=database2)
cursor2 = conn2.cursor()

eventID = cursor2.execute("SELECT eventID FROM events WHERE currentEvent = 1")
eventID = cursor2.fetchone()[0]

if noCE == 'true':
    query = f"SELECT * from {tableName}"
else:
    query = f"SELECT * from {tableName} WHERE eventID = {eventID}"
cursor1.execute(query)
columns = [column[0] for column in cursor1.description]
sourceData = cursor1.fetchall()
print(f"syncing table '{tableName}'")

for row in sourceData:
    cols = ", ".join([col + ' = "' + str(val) + '"' for col, val in zip(columns[1:], row[1:])])
    updateQuery = f"UPDATE {tableName} SET {cols} WHERE {uniqueID}  = {row[0]}"
    updateQuery = re.sub(r'"None"', 'NULL', updateQuery)
    cursor2.execute(updateQuery)
    conn2.commit()

cursor1.close()
conn1.close()
cursor2.close()
conn2.close()

print(f"sync of '{tableName}' complete")
