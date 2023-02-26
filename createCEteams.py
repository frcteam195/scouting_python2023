from optparse import Values
import mysql.connector
import sys
import argparse
import configparser

parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host

config = configparser.ConfigParser()
config.read('helpers/config.ini')

# Get the database login information from the configuration (ini) file
host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

cursor.execute("SELECT eventID FROM events WHERE currentEvent = 1")
currentEventID = str(cursor.fetchone()[0])
print("Current event ID = " + currentEventID)

cursor.execute("DELETE FROM pit where eventID = " + currentEventID)
conn.commit()
cursor.execute("DELETE FROM teams where eventID = " + currentEventID)
conn.commit()

cursor.execute("SELECT team, teamName, teamLocation FROM BAteams")
rows = cursor.fetchall()
for row in rows:
    team = row[0]
    name = row[1]
    location = row[2]
    query = f"INSERT INTO teams (team, eventID, teamName, teamLocation) VALUES ('{team}', '{currentEventID}', '{name}', '{location}')"
    query2 = f"INSERT INTO pit (team, eventID) VALUES ('{team}', '{currentEventID}')"
    print(f"adding team: {team}")
    cursor.execute(query)
    conn.commit()
    cursor.execute(query2)
    conn.commit()

