import mysql.connector
import tbapy
import sys
import getopt
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

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

eventID = cursor.execute("SELECT eventID FROM events WHERE currentEvent = 1")
eventID = cursor.fetchone()[0]

cursor.execute("SELECT * FROM BAmatchData")
BAmatchInfo = cursor.fetchall()

matchInfo = cursor.execute("SELECT * FROM matches WHERE eventID = " + str(eventID))
matchInfo = cursor.fetchall()

print(len(BAmatchInfo))

for i in range(len(BAmatchInfo)):
    print(matchInfo[i][24])
    quit()
    if(BAmatchInfo[i][44] is None):
        query = (f"UPDATE matchScouting SET BAfouls = {str(matchInfo[i][44])}")
