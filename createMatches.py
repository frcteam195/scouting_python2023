import mysql.connector
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

# Get data form events table about the current event
query = "SELECT eventID, BAeventID FROM events WHERE currentEvent = 1"
cursor.execute(query)
eventData = cursor.fetchall()
print(f"eventID, BAeventID = {eventData}")
eventID = eventData[0][0]
BAeventID = eventData[0][1]

# fetch match records from BAschedule table
query = "SELECT * FROM BAschedule"
cursor.execute(query)
rsBAmatches = cursor.fetchall()
#print(rsBAmatches)

# Abort if BAeventID in the BAschedule table has no records for the BAeventID in the events table for the current event
if  rsBAmatches[0][7] != BAeventID:
    print("BAeventIDs do not match between BAschedule table and the currentEvent from the events table")
    print("Aborting!")
    quit()

# Test how many rows exist in the matches table and BAschedule table for the currentEvent
query = "SELECT COUNT(*) FROM BAschedule"
cursor.execute(query)
countBAschedule = cursor.fetchall()
#print(f"countBAschedule = {countBAschedule}")

query = f"SELECT COUNT(*) FROM matches WHERE eventID = {eventID}"
cursor.execute(query)
countCEmatches = cursor.fetchall()
#print(f"countCEmatches = {countCEmatches}")

# Sanity check to be sure there are fewer existing records in the matches table for the current event than there are in the BAschedule table
if countCEmatches[0][0] > countBAschedule[0][0]:
    print(f"There are more matches in the matches table ({countCEmatches[0][0]}) than")
    print(f"the BAschedule table ({countBAschedule[0][0]}) for the current eventID ({eventID}, {BAeventID})")
    print("That should not happen. Aborting! Fix the issue manually and run again")
    print("Go to DataGrip and manually delete the excess matches. You only delete those in excess of the BAschedule table #")
    print("Then reset the index of the match table by running the following command in DataGrip, replacing xxx with the correct index #")
    print("ALTER TABLE matches AUTO_INCREMENT = xxx;")
    quit()

# Find matches from the matches table and add new records to the matchScouting table if they do not already exist
# note: each match is checked individually to see if it exists, In this way, we can start with a few # of matches 
#       in the BAschedule table and just add new matches to the matches table as they are added to the BAschedule table
for row in rsBAmatches:
    rsMatchRecord = {'eventID': eventID, 'matchNum': row[0],
                    'red1': row[1], 'red2': row[2], 'red3': row[3],
                    'blue1': row[4], 'blue2': row[5], 'blue3': row[6]}
    # print(rsMatchRecord)
    query = "SELECT COUNT(*) FROM matches WHERE matches.matchNum = " \
        + str(row[0]) + " AND matches.eventID = " + str(eventID) + ";"
    cursor.execute(query)
    count = cursor.fetchall()
    if count[0][0] == 0:
        items = rsMatchRecord.items()
        columns = str(tuple([x[0] for x in items])).replace("'", "")
        values = str(tuple([x[1] for x in items]))
        print(f"Adding new match: {rsMatchRecord}")
        cursor.execute("INSERT INTO matches " + columns + " VALUES " + values + ";")
        conn.commit()

# Fix Team numbers for the six alliance members. This is good in case a team number changed or was entered incorrectly
print()
print("Running update to fix any team numbers that may have changed, such as a fixed typo in the BAschedule table")
updateQuery = "UPDATE matches INNER JOIN BAschedule ON (matches.matchNum = BAschedule.matchNum) " \
            "SET matches.red1 = BAschedule.red1, " \
            "matches.red2 = BAschedule.red2, " \
            "matches.red3 = BAschedule.red3, " \
            "matches.blue1 = BAschedule.blue1, " \
            "matches.blue2 = BAschedule.blue2, " \
            "matches.blue3 = BAschedule.blue3 " \
            "WHERE matches.eventID = " + str(eventID) + " ;"
cursor.execute(updateQuery)
conn.commit()

cursor.close()
conn.close()
