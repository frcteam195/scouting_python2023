import configparser
import mariadb as mariaDB

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the database login information from the configuration file
host = config['aws-dev1']['host']
user = config['aws-dev1']['user']
passwd = config['aws-dev1']['passwd']
database = config['aws-dev1']['database']

print (host + " " + user + " " + passwd + " " + database)

conn = mariaDB.connect(user=user, passwd=passwd, host=host, database=database)
cursor = conn.cursor()

query = "select BAeventID from eventsAll;"
print (query)

cursor.execute(query)
results = cursor.fetchall()
print (results)
