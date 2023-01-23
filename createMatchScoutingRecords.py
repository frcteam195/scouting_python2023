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

# Find matches from the matches table and add new records to the matchScouting table if they do not already exist
for row in rsMatches:
    i = 1
    while i <= 6:
        rsMatchScoutingRecord = {'matchID': row[0], 'eventID': row[1], 'team': row[i + 2], 'AllianceStationID': str(i)}
        print(rsMatchScoutingRecord)
        items = rsMatchScoutingRecord.items()
        columns = str(tuple([x[0] for x in items])).replace("'", "")
        values = str(tuple([x[1] for x in items]))
        print(columns)
        print(values)
        cursor.execute("INSERT INTO MatchScouting "
                       + columns + " VALUES "
                       + values + ";")
        conn.commit()
        i += 1


# Fix Team #s for the six alliance stations. This is good in case a team number changed or was entered incorrectly
updateQuery = "UPDATE MatchScouting INNER JOIN Matches ON (MatchScouting.MatchID = Matches.MatchID) " \
              "INNER JOIN Events ON (Events.EventID = Matches.EventID) " \
              "SET MatchScouting.Team = Matches.RedTeam1 " \
              "WHERE Events.CurrentEvent = 1 AND MatchScouting.AllianceStationID = 1"
cursor.execute(updateQuery)
conn.commit()

updateQuery = "UPDATE MatchScouting INNER JOIN Matches ON (MatchScouting.MatchID = Matches.MatchID) " \
              "INNER JOIN Events ON (Events.EventID = Matches.EventID) " \
              "SET MatchScouting.Team = Matches.RedTeam2 " \
              "WHERE Events.CurrentEvent = 1 AND MatchScouting.AllianceStationID = 2"
cursor.execute(updateQuery)
conn.commit()

updateQuery = "UPDATE MatchScouting INNER JOIN Matches ON (MatchScouting.MatchID = Matches.MatchID) " \
              "INNER JOIN Events ON (Events.EventID = Matches.EventID) " \
              "SET MatchScouting.Team = Matches.RedTeam3 " \
              "WHERE Events.CurrentEvent = 1 AND MatchScouting.AllianceStationID = 3"
cursor.execute(updateQuery)
conn.commit()

updateQuery = "UPDATE MatchScouting INNER JOIN Matches ON (MatchScouting.MatchID = Matches.MatchID) " \
              "INNER JOIN Events ON (Events.EventID = Matches.EventID) " \
              "SET MatchScouting.Team = Matches.BlueTeam1 " \
              "WHERE Events.CurrentEvent = 1 AND MatchScouting.AllianceStationID = 4"
cursor.execute(updateQuery)
conn.commit()

updateQuery = "UPDATE MatchScouting INNER JOIN Matches ON (MatchScouting.MatchID = Matches.MatchID) " \
              "INNER JOIN Events ON (Events.EventID = Matches.EventID) " \
              "SET MatchScouting.Team = Matches.BlueTeam2 " \
              "WHERE Events.CurrentEvent = 1 AND MatchScouting.AllianceStationID = 5"
cursor.execute(updateQuery)
conn.commit()

updateQuery = "UPDATE MatchScouting INNER JOIN Matches ON (MatchScouting.MatchID = Matches.MatchID) " \
              "INNER JOIN Events ON (Events.EventID = Matches.EventID) " \
              "SET MatchScouting.Team = Matches.BlueTeam3 " \
              "WHERE Events.CurrentEvent = 1 AND MatchScouting.AllianceStationID = 6"
cursor.execute(updateQuery)
conn.commit()


# add team match numbers by looping back through each teams matches and counting
cursor.execute("SELECT DISTINCT MatchScouting.Team "
               "FROM MatchScouting INNER JOIN Events ON MatchScouting.EventID = Events.EventID "
               "AND ((Events.CurrentEvent) = 1) "
               "ORDER BY MatchScouting.Team; ")
rsTeams = cursor.fetchall()
# print(rsTeams)

for team in rsTeams:
    # print(team[0])
    cursor.execute("SELECT MatchScouting.MatchScoutingID FROM MatchScouting INNER JOIN Events "
                   "ON MatchScouting.EventID = Events.EventID AND ((Events.CurrentEvent) = 1) "
                   "WHERE MatchScouting.Team = "
                   + team[0] + " ORDER BY MatchScouting.MatchScoutingID; ")
    rsTeamMatchScouting = cursor.fetchall()
    # print(rsTeamMatchScouting)
    matchNum = 0
    for match in rsTeamMatchScouting:
        matchNum += 1
        # print(match[0])
        query = "UPDATE MatchScouting SET MatchScouting.TeamMatchNo = " + str(matchNum) + " WHERE MatchScouting.MatchScoutingID = " + str(match[0]) + ";"
        # print(query)
        cursor.execute(query)
        conn.commit()
