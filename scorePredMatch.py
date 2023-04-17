import mysql.connector
import sys
import argparse
import configparser
from scorePredMatchAlgorithm import scorePredMatchAlgorithm

# parser to choose the database where the table will be written
parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
parser.add_argument("-red1", "--red1", help = "Enter red1", required=True)
parser.add_argument("-red2", "--red2", help = "Enter red2", required=True)
parser.add_argument("-red3", "--red3", help = "Enter red3", required=True)
parser.add_argument("-blue1", "--blue1", help = "Enter blue1", required=True)
parser.add_argument("-blue2", "--blue2", help = "Enter blue2", required=True)
parser.add_argument("-blue3", "--blue3", help = "Enter blue3", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host
red1 = args.red1
red2 = args.red2
red3 = args.red3
blue1 = args.blue1
blue2 = args.blue2
blue3 = args.blue3

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
        f"WHERE team IN ('{red1}', '{red2}', '{red3}') and eventID = {eventID}"
cursor.execute(query)
redAllianceData = cursor.fetchall()

# get blue alliance data from CEanalysisGraphs
query = f"SELECT team, autoScoreMean, autoScoreStd, " \
        f"autoRampMean, autoRampStd, " \
        f"teleScoreMean, teleScoreStd, " \
        f"rampMean, rampStd " \
        f"FROM CEanalysisGraphs " \
        f"WHERE team IN ('{blue1}', '{blue2}', '{blue3}') and eventID = {eventID}"
cursor.execute(query)
blueAllianceData = cursor.fetchall()

winProb = scorePredMatchAlgorithm(redAllianceData, blueAllianceData)
print(winProb)

cursor.close()
conn.close()
