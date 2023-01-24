import mysql.connector
import sys
import getopt
import sys
import argparse
import configparser
import random

# parser to choose the database where the table will be written
parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host

# Read the configuration file
config = configparser.ConfigParser()
config.read('../helpers/config.ini')

# Get the database login information from the configuration (ini) file
host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

def wipeFakeData():
        cursor.execute("DELETE FROM matchScoutingTest;")
        cursor.execute("ALTER TABLE matchScoutingTest AUTO_INCREMENT = 1;")
        conn.commit()
wipeFakeData()

for i in range(6):
        ramp = 0
        if(i % 3 == 0):
                ramp = 3
        query = "INSERT INTO matchScoutingTest (eventId, matchID, matchNum, team, allianceStationID, preStartPos, preLoad, preNoShow, autoMB, autoRamp, autoPen) VALUES" + \
                "('" + str(1) + \
                "','" + str(1) + \
                "','" + str(1) + \
                "','" + str(195) + \
                "','" + str(i+1) + \
                "','" + str(random.randint(0,3)) + \
                "','" + str(random.randint(0,1)) + \
                "','" + str(0) + \
                "','" + str(random.randint(0,2)) + \
                "','" + str(ramp) + \
                "','" + str(0) + \
                "');"
        print(query)
        #quit()
        cursor.execute(query)
        conn.commit()

cursor.close()
conn.close()