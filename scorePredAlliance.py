import mysql.connector
import sys
import argparse
import configparser
from scorePredAllianceAlgorithm import scorePredAllianceAlgorithm

# parser to choose the database where the table will be written
parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
parser.add_argument("-team1", "--team1", help = "Enter team1", required=True)
parser.add_argument("-team2", "--team2", help = "Enter team2", required=True)
parser.add_argument("-team3", "--team3", help = "Enter team3", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host
team1 = args.team1
team2 = args.team2
team3 = args.team3

config = configparser.ConfigParser()
config.read('helpers/config.ini')

host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

query = "SELECT eventID, BAeventID FROM events WHERE currentEvent = 1"
cursor.execute(query)
eventData = cursor.fetchall()
eventID = eventData[0][0]

# get red alliance data from CEanalysisGraphs
query = f"SELECT team, autoScoreMean, autoScoreStd, " \
        f"autoRampMean, autoRampStd, " \
        f"teleScoreMean, teleScoreStd, " \
        f"rampMean, rampStd " \
        f"FROM CEanalysisGraphs " \
        f"WHERE team IN ('{team1}', '{team2}', '{team3}') and eventID = {eventID}"
print(query)
cursor.execute(query)
allianceData = cursor.fetchall()

score = scorePredAllianceAlgorithm(allianceData)
print(score)

cursor.close()
conn.close()
