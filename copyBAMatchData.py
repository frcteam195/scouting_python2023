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
#print(host + " " + user + " " + passwd + " " + database)

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

CEventID = cursor.execute("SELECT eventID FROM events WHERE currentEvent = 1")
CEventID = cursor.fetchone()[0]

M_table = "matches"
BAMD_table = "BAmatchData"

query = ("UPDATE " + M_table + " "
        "INNER JOIN " + BAMD_table + " ON " + M_table + ".matchNum = " + BAMD_table + ".matchNum "
        "SET matches.redAutoPts = BAmatchData.redAutoPoints, matches.blueAutoPts = BAmatchData.blueAutoPoints, "
        "matches.redTelePts = BAmatchData.redTelePoints, matches.blueTelePts = BAmatchData.blueTelePoints, "
        "matches.redEndGmPts = BAmatchData.redChargeStationPoints, matches.blueEndGmPts = BAmatchData.blueChargeStationPoints, "
        "matches.redScore = BAmatchData.redScore, matches.blueScore = BAmatchData.blueScore, "
        "matches.redFouls = BAmatchData.redFouls, matches.blueFouls = BAmatchData.blueFouls, "
        "matches.redTechFouls = BAmatchData.redTechFouls, matches.blueTechFouls = BAmatchData.blueTechFouls, "
        "matches.redLinksRP = BAmatchData.redLinksRP, matches.blueLinksRP = BAmatchData.blueLinksRP, "
        "matches.redChrgZoneRP = BAmatchData.redChargeStationRP, matches.blueChrgZoneRP = BAmatchData.blueChargeStationRP, "
        "matches.matchTime = BAmatchData.matchTime, "
        "matches.actualTime = BAmatchData.actualTime "
        "WHERE matches.eventID = " + str(CEventID) + ";")
print(query)
cursor.execute(query)
conn.commit()
