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

# def wipeFakeData():
#         cursor.execute("DELETE FROM matchScoutingTest;")
#         cursor.execute("ALTER TABLE matchScoutingTest AUTO_INCREMENT = 1;")
#         conn.commit()
# wipeFakeData()

# cursor.execute("SELECT DISTINCT matchScoutingTest.scoutingStatus "
#                "FROM matchScoutingTest INNER JOIN events ON matchScoutingTest.eventID = events.id "
#                "AND ((events.currentEvent) = 1) "
#                "ORDER BY matchScoutingTest.scoutingStatus; ")
def randomnumber(lower,upper):
        return random.randint(lower,upper)

dictionary = {
        'scoutingStatus':{'type': int, 'default': 0,      'min': 1, 'max': 2},
        'ramp':          {'type': int, 'default': 'NULL', 'min': 0, 'max': 5},
        'autoPen':       {'type': int, 'default': 0,      'min': 0, 'max': 2},
        'rampStartTime': {'type': int, 'default': 'NULL', 'min': 0, 'max': 150} 

}
name = 'ramp'
print(randomnumber(dictionary[name]['min'],
                   dictionary[name]['max']))
quit()
query = "SELECT * FROM matchScoutingTest WHERE scoutingStatus = 0;"
print(query)
quit()
cursor.execute(query)
rsScoutingID = cursor.fetchall()

# for i in range(6):
#         ramp = 0
#         if(i % 3 == 0):
#                 ramp = 3
#         query = "INSERT INTO matchScoutingTest (preStartPos, preLoad, preNoShow, autoMB, autoRamp, autoPen) VALUES" + \
#                 "('"  + str(random.randint(0,3)) + \
#                 "','" + str(random.randint(0,1)) + \
#                 "','" + str(0) + \
#                 "','" + str(random.randint(0,2)) + \
#                 "','" + str(ramp) + \
#                 "','" + str(0) + \
#                 "');"
#         print(query)
#         #quit()
#         cursor.execute(query)
#         conn.commit()

cursor.close()
conn.close()