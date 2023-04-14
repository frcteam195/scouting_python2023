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

tba = tbapy.TBA('Tfr7kbOvWrw0kpnVp5OjeY780ANkzVMyQBZ23xiITUkFo9hWqzOuZVlL3Uy6mLrz')

def sortbyteam(d):
    return d.get('team_number', None)

teamList = []
cursor.execute("SELECT events.BAeventID FROM events WHERE events.currentEvent = 1")
event = cursor.fetchone()[0]
print ("Grabbing teams for the " + event + " event")

cursor.execute("DELETE FROM BAteams")
conn.commit()

eventTeams = tba.event_teams(event)
for team in sorted(eventTeams, key=sortbyteam):
	tempNick = ''
	location = str(team.city) + ', ' + str(team.state_prov) + ', ' + str(team.country)
	if len(location) > 50:
		location = location[:40]
	teams = [team.team_number, team.nickname, location]
	teamList.append(teams)
	for char in team.nickname:
		if char.isalnum() or char == ' ':
			tempNick += char
	values = "(" + str(team.team_number) + "," + team.nickname + "," + location + ")"
	query = "INSERT INTO BAteams (team, teamName, teamLocation) VALUES " + "('" + str(team.team_number) + \
				"','" + tempNick + "','" + str(location) + "')"
	print(query)

	cursor.execute(query)
	conn.commit()

cursor.close()
conn.close()


