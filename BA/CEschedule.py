import mysql.connector
import tbapy
import sys
import getopt
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
config.read('../helpers/config.ini')

# Get the database login information from the configuration (ini) file
host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']
#print(host + " " + user + " " + passwd + " " + database)

conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

tba = tbapy.TBA('Tfr7kbOvWrw0kpnVp5OjeY780ANkzVMyQBZ23xiITUkFo9hWqzOuZVlL3Uy6mLrz')

def sortbymatch(d):
    return d.get('match_number', None)


cursor.execute("SELECT events.BAeventID FROM events WHERE events.currentEvent = 1;")
event = str(cursor.fetchone()[0])
print(event)

eventMatchListRed = []
eventMatchListBlue = []
matchNumberList = []
eventMatches = tba.event_matches(event)


cursor.execute("DELETE FROM BAschedule")
cursor.execute("ALTER TABLE BAschedule AUTO_INCREMENT = 1;")
conn.commit()

for match in eventMatches:
    if match.comp_level == 'qm':
        matchNumberList.append(match.match_number)
matchNumberList = sorted(matchNumberList)

for match in sorted(eventMatches, key=sortbymatch):
    if match.comp_level == 'qm':
        matchNumber = {}
        matchNumber['blue'] = match.alliances.get('blue').get('team_keys')
        matchNumber['blue'] = [key.replace('frc', '') for key in matchNumber['blue']]
        eventMatchListBlue.append(matchNumber)
# print(eventMatchListBlue)

for match in sorted(eventMatches, key=sortbymatch):
    if match.comp_level == 'qm':
        matchNumber = {}
        matchNumber['red'] = match.alliances.get('red').get('team_keys')
        matchNumber['red'] = [key.replace('frc', '') for key in matchNumber['red']]
        eventMatchListRed.append(matchNumber)
# print(eventMatchListRed)

for match in matchNumberList:
    red1 = eventMatchListRed[match - 1].get('red')[0]
    red2 = eventMatchListRed[match - 1].get('red')[1]
    red3 = eventMatchListRed[match - 1].get('red')[2]
    blue1 = eventMatchListBlue[match - 1].get('blue')[0]
    blue2 = eventMatchListBlue[match - 1].get('blue')[1]
    blue3 = eventMatchListBlue[match - 1].get('blue')[2]
    query = "INSERT INTO BAschedule (matchNum, red1, red2, red3, " \
            "blue1, blue2, blue3, BAeventID) VALUES " + \
            "('" + str(match) + "', '" + str(red1) + "', '" + str(red2) + "', '" + str(red3) + "', '" + \
            str(blue1) + "', '" + str(blue2) + "', '" + str(blue3) + "', '" + str(event) + "');"
    print(query)
    
    cursor.execute(query)
    conn.commit()

cursor.close()
conn.close()

