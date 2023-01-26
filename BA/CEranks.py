import mysql.connector
import tbapy
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

cursor.execute("DELETE FROM BAranks;")
cursor.execute("ALTER TABLE BAranks AUTO_INCREMENT = 1;")
conn.commit()

# get the BAeventID for the currentEvent
cursor.execute("SELECT events.BAeventID FROM events WHERE events.currentEvent = 1;")
currentEvent = cursor.fetchone()[0]

eventTeams = tba.event_teams(currentEvent)
teamRanks = tba.event_rankings(currentEvent).get('rankings')
teamRankList = []

print("Writing Ranks to BAranks table")

cursor.execute("DELETE FROM BAranks")
cursor.execute("ALTER TABLE BAranks AUTO_INCREMENT = 1;")
conn.commit()

for teamRank in teamRanks:
    teamRankList.append(teamRank['team_key'][3:])

for team in teamRankList:
    query = "INSERT INTO BAranks (team, rank) VALUES " + "('" + str(team) + "', '" + \
            str(teamRankList.index(team) + 1) + "');"
    cursor.execute(query)
    conn.commit()

print("finished!")

cursor.close()
conn.close()
    

