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

matchTable = "matches"
BAMDtable = "BAmatchData"

query = ("UPDATE " + matchTable + " "
        "INNER JOIN " + BAMDtable + " ON " + matchTable + ".matchNum = " + BAMDtable + ".matchNum "
        "SET matches.redAutoPts = BAmatchData.redAutoPts, matches.blueAutoPts = BAmatchData.blueAutoPts, "
        "matches.redTelePts = BAmatchData.redTelePts, matches.blueTelePts = BAmatchData.blueTelePts, "
        "matches.redTotalCSPts = BAmatchData.redTotalCSPts, matches.blueTotalCSPts = BAmatchData.blueTotalCSPts, "
        "matches.redTotalPts = BAmatchData.redTotalPts, matches.blueTotalPts = BAmatchData.blueTotalPts, "
        "matches.redFouls = BAmatchData.redFouls, matches.blueFouls = BAmatchData.blueFouls, "
        "matches.redTechFouls = BAmatchData.redTechFouls, matches.blueTechFouls = BAmatchData.blueTechFouls, "
        "matches.redSustainabilityBonus = BAmatchData.redSustainabilityBonus, matches.blueSustainabilityBonus = BAmatchData.blueSustainabilityBonus, "
        "matches.redActivationBonus = BAmatchData.redActivationBonus, matches.blueActivationBonus = BAmatchData.blueActivationBonus, "
        "matches.redLinkPts = BAmatchData.redLinkPts, matches.blueLinkPts = BAmatchData.blueLinkPts, "
        "matches.redCoopGamePieceCount = BAmatchData.redCoopGamePieceCount, matches.blueCoopGamePieceCount = BAmatchData.blueCoopGamePieceCount, "
        "matches.redCoopertitionBonus = BAmatchData.redCoopertitionBonus, matches.blueCoopertitionBonus = BAmatchData.blueCoopertitionBonus, "
        "matches.redAutoMoveBonusPts = BAmatchData.redAutoMoveBonusPts, matches.blueAutoMoveBonusPts = BAmatchData.blueAutoMoveBonusPts, "
        "matches.redAutoGamePieces = BAmatchData.redAutoGamePieces, matches.blueAutoGamePieces = BAmatchData.blueAutoGamePieces, "
        "matches.redAutoGamePiecePts = BAmatchData.redAutoGamePiecePts, matches.blueAutoGamePiecePts = BAmatchData.blueAutoGamePiecePts, "
        "matches.redAutoCSPts = BAmatchData.redAutoCSPts, matches.blueAutoCSPts = BAmatchData.blueAutoCSPts, "
        "matches.redTeleGamePieces = BAmatchData.redTeleGamePieces, matches.blueTeleGamePieces = BAmatchData.blueTeleGamePieces, "
        "matches.redTeleGamePiecePts = BAmatchData.redTeleGamePiecePts, matches.blueTeleGamePiecePts = BAmatchData.blueTeleGamePiecePts, "
        "matches.redEndgameCSPts = BAmatchData.redEndgameCSPts, matches.blueEndgameCSPts = BAmatchData.blueEndgameCSPts, "
        "matches.matchTime = BAmatchData.matchTime, "
        "matches.actualTime = BAmatchData.actualTime "
        "WHERE matches.eventID = " + str(eventID))

cursor.execute(query)
conn.commit()

print("copyBAmatchData complete")

cursor.close()
conn.close()
