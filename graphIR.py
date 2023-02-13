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
query = f"DELETE FROM {CEAG_table}"
cursor.execute(query)
conn.commit()

print("Time: %0.2f seconds" % (time.time() - start_time))
print()

# 1,startingPosition
# 2,autoScore - autoScoreMean & autoScoreMedian
# 3,autoGamePieces - autoGamePiecesMean & autoGamePiecesMedian
# 4,autoRamp - autoRampMean & autoRampMedian
# 5,teleHigh - teleHighMean & teleHighMedian
# 6,teleMid - teleMidMean & teleMidMedian
# 7,teleLow - teleLowMean & teleLowMedian
# 8,teleTotal - teleTotalMean & teleTotalMedian
# 9,teleCones 
# 10,teleCubes
# 11,teleCommunity - teleCommunityMean & teleCommunityMedian
# 12,teleLZPickup - teleLZPickupMean & teleLZPickupMedian
# 15,ramp - rampMean & rampMedian
# 16,rampPos
# 17,postSubBroke
# 18,postBrokeDown
# 19,postReorientCone
# 20,postShelfPickup
# 21,postGroundPickup
# 22,postGoodPartner

# insert first record for analysisType 7 which is the first one in the CEanalysisGraphs table
query = (f"INSERT INTO {CEAG_table} (team, eventID, teleLowMean, teleLowMedian) " \
          "SELECT team, eventID, S1V, S2V FROM CEanalysis WHERE analysisTypeID = 7")
print(query)
cursor.execute(query)
conn.commit()

# loop through additional analysisTypes besides #7 which was performed with the insert
analysisTypeList = [6, 5]
analysisNameList = ["teleMidMean", \
                    "teleHighMean", \
                    # Split between means and medians
                    "teleMidMedian", \
                    "teleHighMedian"]
print(analysisNameList)
print(len(analysisNameList))
print(len(analysisTypeList))
for i in range(len(analysisTypeList)):
    print(f"i = {i}")
    # query = (
            # f"UPDATE {CEAG_table} INNER JOIN CEanalysis ON {CEAG_table}.team = CEanalysis.team AND {CEAG_table}.eventID = CEanalysis.eventID "
            # f"SET {analysisNameList[i]} CEanalysis.S1V, {analysisNameList[i + 2]} CEanalysis.S2V, "
            # f"WHERE CEanalysis.analysisTypeID = {str(analysisTypeList[i])}"
    # )
    query = ("UPDATE " + CEAG_table + " INNER JOIN CEanalysis ON " + CEAG_table + ".team = CEanalysis.team " \
             "AND " + CEAG_table + ".eventID = CEanalysis.eventID " \
             "SET " + analysisNameList[i] + " = CEanalysis.S1V, " \
             + analysisNameList[i+2] + " = CEanalysis.S2V " \
             "WHERE CEanalysis.analysisTypeID = " + str(analysisTypeList[i]))
    print(query)