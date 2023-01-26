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

cursor.execute("DELETE FROM BAoprs;")
cursor.execute("ALTER TABLE BAoprs AUTO_INCREMENT = 1;")
conn.commit()

# get the BAeventID for the currentEvent
cursor.execute("SELECT events.BAeventID FROM events WHERE events.currentEvent = 1;")
currentEvent = cursor.fetchone()[0]

eventTeams = tba.event_teams(currentEvent)
eventOpr = tba.event_oprs(currentEvent).get("oprs")

eventOPRSorted = [(k[3:], eventOpr[k]) for k in sorted(eventOpr, key=eventOpr.get, reverse=True)]
# print(eventOPRSorted)

print('Writing OPRs to BAoprs table')

for team in eventOPRSorted:
    query = "INSERT INTO BAoprs (team, OPR) VALUES " + "('" + str(team[0]) + "', '" + str(team[1]) + "');"
    # print(query)
    cursor.execute(query)
    conn.commit()
print('finished!')

cursor.close()
conn.close()
