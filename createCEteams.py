import mariadb as mariaDB
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

conn = mariaDB.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()


cursor.execute("SELECT events.id FROM events WHERE events.currentEvent = 1;")
event = str(cursor.fetchone()[0])
print(event)

# cursor.execute("DELETE FROM CurrentEventTeams;")
# cursor.execute("ALTER TABLE CurrentEventTeams AUTO_INCREMENT = 1;")
# conn.commit()

cursor.execute("SELECT BA_CEteams.Team FROM BA_CEteams")
for team in cursor.fetchall():
    query = "INSERT INTO teams (team) VALUES (" + team[0] + ");"
    print(query)
    cursor.execute(query)
    conn.commit()