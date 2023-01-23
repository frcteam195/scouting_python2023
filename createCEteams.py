import mysql.connector
import sys
import argparse
import configparser

# parser to choose the database where the table will be written
parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host

# Read the configuration file
config = configparser.ConfigParser()
config.read('helpers/config.ini')

# Get the database login information from the configuration (ini) file
host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']
#print(host + " " + user + " " + passwd + " " + database)

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

cursor.execute("SELECT id FROM events WHERE currentEvent = 1")
currentEventID = str(cursor.fetchone()[0])
print("Current event ID = " + currentEventID)

cursor.execute("DELETE FROM teams where eventID = " + currentEventID)
conn.commit()

cursor.execute("SELECT team, teamName, teamLocation FROM BAteams")
rows = cursor.fetchall()
for row in rows:
    team = row[0]
    name = row[1]
    location = row[2]
    query = f"INSERT INTO teams (team, eventID, teamName, teamLocation) VALUES ('{team}', '{currentEventID}', '{name}', '{location}')"
    print(query)
    cursor.execute(query)
    conn.commit()

cursor.close()
conn.close()