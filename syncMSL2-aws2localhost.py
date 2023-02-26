import mysql.connector
import sys
import getopt
import sys
import argparse
import configparser

tableName = 'matchScoutingL2'
AWSdatabase = 'dev2'
localDatbase = 'testing'
uniqueID = 'matchScoutingL2ID'

# Read the configuration file
config = configparser.ConfigParser()
config.read('helpers/config.ini')

# Get the database login information from the configuration (ini) file
AWShost = config['aws-'+AWSdatabase]['host']
AWSuser = config['aws-'+AWSdatabase]['user']
AWSpasswd = config['aws-'+AWSdatabase]['passwd']
AWSdatabase = config['aws-'+AWSdatabase]['database']
# localHost = config['localhost-'+localDatbase]['host']
# localUser = config['localhost-'+localDatbase]['user']
# localPasswd = config['localhost-'+localDatbase]['passwd']
# localDatabase = config['localhost-'+localDatbase]['database']
# remove the next four lines and uncomment above four lines when on localhost computer
localHost = config['aws-'+localDatbase]['host']
localUser = config['aws-'+localDatbase]['user']
localPasswd = config['aws-'+localDatbase]['passwd']
localDatabase = config['aws-'+localDatbase]['database']

AWSConn = mysql.connector.connect(user=AWSuser, passwd=AWSpasswd, host=AWShost, database=AWSdatabase)
AWSCursor = AWSConn.cursor()
localConn = mysql.connector.connect(user=localUser, passwd=localPasswd, host=localHost, database=localDatabase)
localCursor = localConn.cursor()

# eventID = localCursor.execute("SELECT eventID FROM events WHERE currentEvent = 1")
# eventID = localCursor.fetchone()[0]
eventID = 1

AWSquery = f"SELECT * from {tableName} WHERE eventID = {eventID}"
AWSCursor.execute(AWSquery)
columns = [column[0] for column in AWSCursor.description]
AWSdata = AWSCursor.fetchall()

for row in AWSdata:
    print(row)
    updateQuery = "UPDATE matchScoutingL2 SET {} WHERE matchScoutingL2ID = {}".format(
        ", ".join([col + " = '" + str(val) + "'" for col, val in zip(columns[1:], row[1:])]), row[0])
    localCursor.execute(updateQuery)
    localConn.commit()


AWSCursor.close()
AWSConn.close()
localCursor.close()
localConn.close()

print("sync complete")

