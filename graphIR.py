import mysql.connector
import numpy as np
import datetime
import time
import argparse
import configparser

# *********************** argument parser **********************
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

# ********** Main program **********
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
start_time = time.time()

CEAG_table = "CEanalysisGraphs"
CEventID = cursor.execute("SELECT eventID FROM events WHERE currentEvent = 1")
CEventID = cursor.fetchone()[0]

query = f"DELETE FROM {CEAG_table} WHERE eventID = {CEventID}"
cursor.execute(query)
conn.commit()

# 1,startingPosition
# 2,autoScore           - #8 -  autoScoreMean & autoScoreMedian
# 3,autoGamePieces      - #9 -  autoGamePiecesMean & autoGamePiecesMedian
# 4,autoRamp            - #10 - autoRampMean & autoRampMedian
# 5,teleHigh            - #3 -  teleHighMean & teleHighMedian
# 6,teleMid             - #2 -  teleMidMean & teleMidMedian
# 7,teleLow             - #1 -  teleLowMean & teleLowMedian
# 8,teleTotal           - #4 -  teleTotalMean & teleTotalMedian
# 9,teleCones 
# 10,teleCubes
# 11,teleCommunity      - #5 -  teleCommunityMean & teleCommunityMedian
# 12,teleLZPickup       - #6 -  teleLZPickupMean & teleLZPickupMedian
# 15,ramp               - #7 -  rampMean & rampMedian
# 16,rampPos
# 17,postSubBroke
# 18,postBrokeDown
# 19,postReorientCone
# 20,postShelfPickup
# 21,postGroundPickup
# 22,postGoodPartner
# 23,matchVideos
# 24,BAFoulsPts
# 25,BARankingPoints
# 26,totalScore
# 27,teleScore



# insert first record for analysisType 7 which is the first one in the CEanalysisGraphs table
query = (f"INSERT INTO {CEAG_table} (team, eventID, teleLowMean, teleLowMedian, teleLowFormat) " \
         f"SELECT team, eventID, S1V, S2V, S3F FROM CEanalysis WHERE analysisTypeID = 7 and eventID = {CEventID}")

cursor.execute(query)
conn.commit()

# loop through additional analysisTypes besides #7 which was performed with the insert
analysisTypeList = [6, 5, 8, 11, 12, 15, 2, 3, 4, 26, 27]
analysisNameList = ["teleMidMean", \
                    "teleHighMean", \
                    "teleTotalMean", \
                    "teleCommunityMean", \
                    "teleLZPickupMean", \
                    "rampMean", \
                    "autoScoreMean", \
                    "autoGamePiecesMean", \
                    "autoRampMean", \
                    "totalScoreMean", \
                    "teleScoreMean", \
                    # Split between means and medians
                    "teleMidMedian", \
                    "teleHighMedian", \
                    "teleTotalMedian", \
                    "teleCommunityMedian", \
                    "teleLZPickupMedian", \
                    "rampMedian", \
                    "autoScoreMedian", \
                    "autoGamePiecesMedian", \
                    "autoRampMedian", \
                    "totalScoreMedian", \
                    "teleScoreMedian", \
                    #
                    "teleMidFormat", \
                    "teleHighFormat", \
                    "teleTotalFormat", \
                    "teleCommunityFormat", \
                    "teleLZPickupFormat", \
                    "rampFormat", \
                    "autoScoreFormat", \
                    "autoGamePiecesFormat", \
                    "autoRampFormat", \
                    "totalScoreFormat", \
                    "teleScoreFormat"]

for i in range(len(analysisTypeList)):
    query = ("UPDATE " + CEAG_table + " INNER JOIN CEanalysis ON " + CEAG_table + ".team = CEanalysis.team " \
             "AND " + CEAG_table + ".eventID = CEanalysis.eventID " \
             "SET " + analysisNameList[i] + " = CEanalysis.S1V, " \
             + analysisNameList[i+(len(analysisTypeList))] + " = CEanalysis.S2V, " \
             + analysisNameList[i+(len(analysisTypeList))+(len(analysisTypeList))] + " = CEanalysis.S3F " \
             "WHERE CEanalysis.analysisTypeID = " + str(analysisTypeList[i]))
    # print(query)
    cursor.execute(query)
    conn.commit()

print("Time: %0.2f seconds" % (time.time() - start_time))

cursor.close()
conn.close()
