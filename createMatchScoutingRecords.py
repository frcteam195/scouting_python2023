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

# Find matches from the matches table and add new records to the matchScouting table
for col in rsMatches:
    i = 1
    while i <= 6:
        rsMatchScoutingRecordExistsTest = {'matchID': col[0], 'eventID': col[1], 'matchNum': col[2], 'allianceStationID': str(i)}
        items = rsMatchScoutingRecordExistsTest.items()
        print(items)
        columns = str(tuple([x[0] for x in items])).replace("'", "")
        print(columns)
        values = str(tuple([x[1] for x in items]))
        print(values)
        query = "SELECT matchID, eventID, matchNum, allianceStationID FROM matchScouting WHERE " + \
                "matchID = " + str(col[0]) + " AND eventID = " + str(col[1]) + \
                " AND matchNum = " + str(col[2]) + " AND allianceStationID = " + str(i)
        print(query)
        cursor.execute(query)
        exists = cursor.fetchall()
        print(f"exists = {exists}")
        if len(exists) == 0:
            print ("length zero")
        else:
            print ("length not zero")
        quit()

       #matchID = 1 AND eventID = 1 AND matchNum = 1 AND team = '3464' AND allianceStationID = '1';
        
        print(f"Adding match record: {rsMatchScoutingRecord}")
        rsMatchScoutingRecord = {'matchID': col[0], 'eventID': col[1], 'matchNum': col[2], 'team': col[i + 2], 'allianceStationID': str(i)}
        items = rsMatchScoutingRecord.items()
        columns = str(tuple([x[0] for x in items])).replace("'", "")
        values = str(tuple([x[1] for x in items]))
        # print(columns)
        # print(values)
        query = "INSERT INTO matchScouting " + columns + " VALUES " + values
        print(query)
        quit()
        cursor.execute(query)
        conn.commit()
        i += 1

# Fix team #s for the six alliance stations. This is good in case a team number changed or was entered incorrectly
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
