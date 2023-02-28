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

cursor.execute("DELETE FROM BAoprs")
conn.commit()

cursor.execute("SELECT events.BAeventID FROM events WHERE events.currentEvent = 1")
BAeventID = cursor.fetchone()[0]

cursor.execute("SELECT events.eventID FROM events WHERE events.currentEvent = 1")
eventID = cursor.fetchone()[0]

#eventTeams = tba.event_teams(BAeventID)
eventOPR = tba.event_oprs(BAeventID).get("oprs")
eventOPRSorted = [(k[3:], eventOPR[k]) for k in sorted(eventOPR, key=eventOPR.get, reverse=True)]

print('Writing OPRs to BAoprs table')

for team in eventOPRSorted:
    query = f"INSERT INTO BAoprs (eventID, team, OPR) VALUES ('{eventID}', '{str(team[0])}', '{str(team[1])}')"
    cursor.execute(query)
    conn.commit()
print('finished!')

cursor.close()
conn.close()
