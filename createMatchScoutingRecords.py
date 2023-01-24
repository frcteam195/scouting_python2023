import mysql.connector
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


query = "SELECT matches.* FROM matches LEFT JOIN matchScouting " \
        "ON (matches.id = matchScouting.eventID) " \
        "AND matches.id = matchScouting.id " \
        "JOIN events ON (events.id = matches.eventID) " \
        "WHERE (((events.currentEvent) = 1) AND ((matchScouting.matchID) is Null))"
#print(query)
cursor.execute(query)
rsMatches = cursor.fetchall()
# print(rsMatches)

# Find matches from the matches table and add new records to the matchScouting table if they do not exist
for col in rsMatches:
    # there will be six matchScoutingRecords / match. Important that the schema in the matches and matchScouting tables
    #   match what this script expects as we are just calling columns #s from each row.
    i = 1
    while i <= 6:
        # we first need to know if a matchScoutingRecord exists for the given match so we do not add a duplicate. This is important
        #   if we need to first build the matches and matchScoutingRecords with an initial limited schedule, say if TBA API is down
        #   or unreachable.
        # we will first check if a record with the same matchID, eventID, matchNum, and allianceStationID exists. Each of those items
        #   is not unique in the matchScouting table, but the combination should be. We are not using team # as if the schedule changed
        #   this could give a false reading. The other 4 items should be solid if the matchScoutingRecord already exists.
        
        # define some variables for easier code below ...
        matchID = col[0]
        eventID = col[1]
        matchNum = col[2]
        allianceStationID = i
        team = col[i+2]
        
        # grab the record to so we can see if it already exists
        rsMatchScoutingRecordExistsTest = {'matchID': matchID, 'eventID': eventID, 'matchNum': matchNum, 'allianceStationID': str(allianceStationID)}
        items = rsMatchScoutingRecordExistsTest.items()
        values = str(tuple([x[1] for x in items]))
        query = "SELECT matchID, eventID, matchNum, allianceStationID FROM matchScouting WHERE " + \
                "matchID = " + str(matchID) + " AND eventID = " + str(eventID) + \
                " AND matchNum = " + str(matchNum) + " AND allianceStationID = " + str(allianceStationID)
        cursor.execute(query)
        exists = cursor.fetchall()
        # if the record exists lets do nothing
        if len(exists) != 0:
            print (f"matchID = {matchID}, eventID = {eventID}, matchNum = {matchNum}, team = {team},\t allianceStationID ={ allianceStationID} EXISTS, doing nothing")
        # if the record does not exist lets grab it again, with team this time, and add it to the matchScouting table
        else:
            print (f"matchID = {matchID}, eventID = {eventID}, matchNum = {matchNum}, team = {team},\t allianceStationID ={ allianceStationID} MISSING, adding now")
            rsMatchScoutingRecord = {'matchID': col[0], 'eventID': col[1], 'matchNum': col[2], 'team': col[i + 2], 'allianceStationID': str(i)}
            items = rsMatchScoutingRecord.items()
            columns = str(tuple([x[0] for x in items])).replace("'", "")
            values = str(tuple([x[1] for x in items]))
            query = "INSERT INTO matchScouting " + columns + " VALUES " + values
            cursor.execute(query)
            conn.commit()
        i += 1


# Fix team #s for the six alliance stations. This is good in case a team number changed or was entered incorrectly
print()
print ("looping through matchScouting records and comparing teams in each record to the matches table")
print ("    fixing team # if different to fix any typos if we had to enter the schedule by hand")
updateQuery = "UPDATE matchScouting INNER JOIN matches ON (matchScouting.matchID = matches.id) " \
              "INNER JOIN events ON (events.id = matches.eventID) " \
              "SET matchScouting.team = matches.red1 " \
              "WHERE events.currentEvent = 1 AND matchScouting.allianceStationID = 1"
cursor.execute(updateQuery)
conn.commit()

updateQuery = "UPDATE matchScouting INNER JOIN matches ON (matchScouting.matchID = matches.id) " \
              "INNER JOIN events ON (events.id = matches.eventID) " \
              "SET matchScouting.team = matches.red2 " \
              "WHERE events.currentEvent = 1 AND matchScouting.allianceStationID = 2"
cursor.execute(updateQuery)
conn.commit()

updateQuery = "UPDATE matchScouting INNER JOIN matches ON (matchScouting.matchID = matches.id) " \
              "INNER JOIN events ON (events.id = matches.eventID) " \
              "SET matchScouting.team = matches.red3 " \
              "WHERE events.currentEvent = 1 AND matchScouting.allianceStationID = 3"
cursor.execute(updateQuery)
conn.commit()

updateQuery = "UPDATE matchScouting INNER JOIN matches ON (matchScouting.matchID = matches.id) " \
              "INNER JOIN events ON (events.id = matches.eventID) " \
              "SET matchScouting.team = matches.blue1 " \
              "WHERE events.currentEvent = 1 AND matchScouting.allianceStationID = 4"
cursor.execute(updateQuery)
conn.commit()

updateQuery = "UPDATE matchScouting INNER JOIN matches ON (matchScouting.matchID = matches.id) " \
              "INNER JOIN events ON (events.id = matches.eventID) " \
              "SET matchScouting.team = matches.blue2 " \
              "WHERE events.currentEvent = 1 AND matchScouting.allianceStationID = 5"
cursor.execute(updateQuery)
conn.commit()

updateQuery = "UPDATE matchScouting INNER JOIN matches ON (matchScouting.matchID = matches.id) " \
              "INNER JOIN events ON (events.id = matches.eventID) " \
              "SET matchScouting.team = matches.blue3 " \
              "WHERE events.currentEvent = 1 AND matchScouting.allianceStationID = 6"
cursor.execute(updateQuery)
conn.commit()


# add team match numbers by looping back through each teams matches and counting
cursor.execute("SELECT DISTINCT matchScouting.team "
               "FROM matchScouting INNER JOIN events ON matchScouting.eventID = events.id "
               "AND ((events.currentEvent) = 1) "
               "ORDER BY matchScouting.team; ")
rsTeams = cursor.fetchall()
# print(rsTeams)

print()
print ("looping through matchScouting records and creating teamMatchNum values")
print ("NOTE: this only works if the added matches to the schedule are in order.")
print ("    if an early match is entered at the end of the matches table then the teamMatchNum will be out of order")
# The above note can be fixed by writing a script to (1) dump the current event records from the matchScouting table
#   to a csv file, (2) deleting them from the matchScouting table, (3) resetting the auto increment index
#   with "ALTER TABLE matchScouting AUTO_INCREMENT = xxx;", (4) sorting the matchScouting records in pandas
#   and saving to a new csv file, and (5) re-importing the csv file with the matchScouting records in the 
#   correct order.
# At this time, this is an unlikely scenerio as matches would lilely be added to the bottom of the schedule
#   and not the top and this script takes care of typos in team numbers already so punting on a more 
#   elagent solution for this likely to never happen scenerio
for team in rsTeams:
    # print(team[0])
    cursor.execute("SELECT matchScouting.id FROM matchScouting INNER JOIN events "
                   "ON matchScouting.eventID = events.id AND ((events.currentEvent) = 1) "
                   "WHERE matchScouting.team = "
                   + team[0] + " ORDER BY matchScouting.id; ")
    rsTeamMatchScouting = cursor.fetchall()
    # print(rsTeamMatchScouting)
    matchNum = 0
    for match in rsTeamMatchScouting:
        matchNum += 1
        # print(match[0])
        query = "UPDATE matchScouting SET matchScouting.teamMatchNum = " + str(matchNum) + \
                " WHERE matchScouting.id = " + str(match[0]) + ";"
        # print(query)
        cursor.execute(query)
        conn.commit()

cursor.close()
conn.close()

print()
print ("finsihed!")
