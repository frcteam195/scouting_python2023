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
try:
    config.read('../helpers/config.ini')
except configparser.Error as e:
    print(e)
    sys.exit(1)

# Get the database login information from the configuration (ini) file
host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']
#print(host + " " + user + " " + passwd + " " + database)

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

data = ("1", "2022cthar", "1", "Hartford", "Hartford, CT, USA", "2022-04-01", "2022-04-02")
print(data)
query = "INSERT INTO events (id, BAeventID, currentEvent, eventName, eventLocation, eventStartDate, eventEndDate) VALUES " + \
        "('" + str(data[0]) + \
        "','" + str(data[1]) + \
        "','" + str(data[2]) + \
        "','" + str(data[3]) + \
        "','" + str(data[4]) + \
        "','" + str(data[5]) + \
        "','" + str(data[6]) + "');"
print(query)

cursor.execute(query)
conn.commit()

cursor.close()
conn.close()
