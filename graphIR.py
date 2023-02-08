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
    

CEAG_table = "CurrentEventAnalysisGraphs"


columns = []
wipeCEAG()
analyze()

print("Time: %0.2f seconds" % (time.time() - start_time))
print()

# Function to run a query - the query string must be passed to the function
def run_query(query):
    cursor.execute(query)

# Function to determine the DB table column headers
def setColumns(columns):
    columns = columns

# Function to wipe the CEAG table. We may want to make this only remove CurrentEvent records.
def wipeCEAG():
    query = f"DELETE FROM {CEAG_table}"
    print(query)
    run_query(query)
    conn.commit()

# Function to write means and medians to the CEAGraphs table
def analyze():
    analysisTypeList = [7, 6, 5]
    analysisNameList = ["teleLowMean, teleLowMedian, teleMidMean, teleMidMedian, teleHighMean, teleHighMedian"]
    run_query("INSERT INTO " + CEAG_table + "(Team, EventID, AutonomousMean, AutonomousMedian, AutonomousFormat) "
                        "SELECT Team, EventID, Summary1Value, Summary2Value, Summary3Format "
                        "FROM CurrentEventAnalysis "
                        "WHERE AnalysisTypeID = 10;")
    for i in range(len(analysisTypeList)):
        #print(i)
        run_query("UPDATE " + CEAG_table + " "
                        "INNER JOIN CurrentEventAnalysis ON " + CEAG_table + ".Team = CurrentEventAnalysis.Team AND " + CEAG_table + ".EventID = CurrentEventAnalysis.EventID "
                        "SET " + analysisNameList[i] + " = CurrentEventAnalysis.Summary1Value, " + analysisNameList[i + 8] + " = CurrentEventAnalysis.Summary2Value, " + analysisNameList[i + 16] + " = CurrentEventAnalysis.Summary3Format "
                        "WHERE CurrentEventAnalysis.AnalysisTypeID = " + str(analysisTypeList[i]) + ";")

    conn.commit()
    
