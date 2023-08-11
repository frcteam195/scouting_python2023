import mysql.connector
import numpy as np
import os
import sys
import datetime
import time
import argparse
import configparser

from analysisTypes import *

level1AnalysisTypesDict = {
                    # "testAnalysis": testAnalysis.testAnalysis,
                    # "pit": pit.pit
                    #"autoScore": autoScore.autoScore
                    "testAnalysis": testAnalysis
                    # "pit": pit
                    }

# parser to choose the database where the table will be written

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
start_time = time.time()
print("This script takes a while, please be patient!", end="\n\n")

parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host

CEA_tmpTable = "CEanalysisTmp"
BAoprTable = "BAoprs"
BArankTable = "BAranks"

# Read the configuration file & set DB login variables
config = configparser.ConfigParser()
if len(config.read('helpers/config.ini')) == 0:
    print("Could not read the file: helpers/config.ini")
    sys.exit("Exiting program")
try:
    host = config[input_host+"-"+input_db]['host']
    user = config[input_host+"-"+input_db]['user']
    passwd = config[input_host+"-"+input_db]['passwd']
    database = config[input_host+"-"+input_db]['database']
except KeyError:
    print("Could not set DB login variables correctly,")
    sys.exit("Exiting! Please check config.ini and try again")

# Make the DB connection
try:
    conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
    cursor = conn.cursor()
except:
    print("Could not connect to database")
    sys.exit("Exiting!")

# Define function for database queries
def runQuery(queryString):
    try:
        cursor.execute(queryString)
    except:
        print(f"SQL query failed: '{queryString}'")
        sys.exit("Exiting program due to SQL query error")

# Drop existing CEanalysisTmp table if it exists (it should not) and rebuild table
queryString = "DROP TABLE IF EXISTS CEanalysisTmp"
runQuery(queryString)
try:
    SQLfile = open('CEanalysisTmp.sql','r')
except IOError:
    print("CEanalysisTmp file could not be opened, aborting!")
    sys.exit()
queryString = SQLfile.read()
runQuery(queryString)

# Get current event from the events table
queryString = "SELECT eventID from events WHERE currentEvent = 1"
runQuery(queryString)
result = cursor.fetchone()
eventID = int(result[0]) if result else None
if eventID == None:
    print("There is no currentEvent in the events table")
    sys.exit("Fix the database table and try again")

# Get teams in a list for current event
queryString = (
    f"SELECT team from matchScouting WHERE eventID = {eventID} "
    f"GROUP BY CAST(team AS INT)"
)
runQuery(queryString)
teams = cursor.fetchall()
# fetchall creates a list of tuples. The line below coverts the list of tuples to integers
teams = [int(tup[0]) for tup in teams]

# Grab data from matchScouting and create a List of Python dictionaries for each matchScouting record
queryString = f"SELECT * from matchScouting WHERE eventID = {eventID}"
runQuery(queryString)
matchScouting = cursor.fetchall()
assert len(matchScouting) > 0, "No matchScouting data found"
column_names = [description[0] for description in cursor.description]
matchScoutingData = [dict(zip(column_names, row)) for row in matchScouting]
for row in matchScoutingData:
    row['team'] = int(row['team'])  # change team from string to int in the list of dictionaries

# def insertAnalysis(rsCEA):
#     keys = ', '.join(rsCEA.keys())
#     values = ', '.join(['"{}"'.format(v) if isinstance(v, str) else str(v) for v in rsCEA.values()])
#     queryString = f"INSERT INTO {CEA_tmpTable} ({keys}) VALUES ({values})"
#     print(queryString)
#     runQuery(queryString)
#     conn.commit()

# Loops through teams
payLoad = []
for team in teams:
    print()
    print(team)
    teamMatchScoutingData = [row for row in matchScoutingData if row['team'] == team]
    if teamMatchScoutingData:
        for analysisType2analyze in level1AnalysisTypesDict:
            print(f"analyzing team {team} using {analysisType2analyze}")
            rsCEA = level1AnalysisTypesDict[analysisType2analyze](teamMatchScoutingData)
            payLoad.append(rsCEA)
            # print(rsCEA)
# print(payLoad)
print(len(payLoad))

if payLoad:
    rsCEA = payLoad[0]
    keys = ', '.join(rsCEA.keys())  # This will extract the column headings from the CEanalysisTmp table
    valueTypes = ', '.join(['%s'] * len(rsCEA))
    queryFormat = f"INSERT INTO {CEA_tmpTable} ({keys}) VALUES ({valueTypes})"
    print(queryFormat)
    queryData = []
    countChecker = 0  # set a counter to zero so we execute a command only on first pass through loop
    for dictionaryRecord in payLoad:
        # print(len(dictionaryRecord))
        # print(dictionaryRecord)
        if countChecker == 0:  # if it is the first pass through the loop set lengthCheck to lenght of first record 
            lengthCheck = len(dictionaryRecord)
        if lengthCheck != len(dictionaryRecord):  # if a record does not equal the lenght of first record abort program
            print(f"The record has {len(dictionaryRecord)} elements and is different from the first record of {lengthCheck}")
            print("There must be an issue with an analysisType as all records should be the same length")
            print("Aborting")
            sys.exit()
        else:
            dataTuple = tuple(dictionaryRecord.values())
            queryData.append(dataTuple)
        countChecker += 1
    print(queryData)
    queryData = [[None if item == '' else item for item in row] for row in queryData]
    print()
    print(queryData)
    cursor.executemany(queryFormat, queryData)
    conn.commit()
    

cursor.close()
conn.close()