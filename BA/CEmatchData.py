import mysql.connector
import tbapy
import argparse
import datetime as dt
import time
import datetime
import pytz
import configparser

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
start_time = time.time()

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

cursor.execute("DELETE FROM BAmatchData;")
conn.commit()

print("Pease be patient! Grabbing lots of data from The Blue Alliance")

cursor.execute("SELECT events.BAeventID FROM events WHERE events.currentEvent = 1")
BAeventID = cursor.fetchone()[0]
cursor.execute("SELECT events.eventID FROM events WHERE events.currentEvent = 1")
eventID = cursor.fetchone()[0]
cursor.execute("SELECT events.timeZone FROM events WHERE events.currentEvent = 1")
timeZone = cursor.fetchone()[0]

qNum = 0
# eventInfo is all the data for all the matches
eventInfo = tba.event_matches(BAeventID)
tz = pytz.timezone(str(timeZone))

# loop through each match from the eventInfo which contains records for all matches and set several variables
for match in eventInfo:
    matchInfo = tba.match(match.key)
    matchNum = matchInfo.match_number
    matchTimeRaw = matchInfo.time
    matchActTimeRaw = matchInfo.actual_time
    matchTime = dt.datetime.fromtimestamp(matchTimeRaw, tz)
    matchAlliances = matchInfo.alliances
    matchRed = matchAlliances["red"]
    matchBlue = matchAlliances["blue"]
    matchRedTeams = matchRed["team_keys"]
    matchBlueTeams = matchBlue["team_keys"]

    if match.comp_level == "qm":
        # note, in the query the 3: subtract away the frc that is in front of each team number
        query = (f"INSERT INTO BAmatchData (matchNum, eventID, matchTime, red1, red2, red3, blue1, blue2, blue3) "
                f"VALUES ({matchNum}, {eventID}, '{str(matchTime)[11:16]}', "
                f"{int(str(matchRedTeams[0])[3:])}, "
                f"{int(str(matchRedTeams[1])[3:])}, "
                f"{int(str(matchRedTeams[2])[3:])}, "
                f"{int(str(matchBlueTeams[0])[3:])}, "
                f"{int(str(matchBlueTeams[1])[3:])}, "
                f"{int(str(matchBlueTeams[2])[3:])})")
        cursor.execute(query)
        conn.commit()

    if matchInfo.actual_time is not None:
        matchActTime = dt.datetime.fromtimestamp(matchActTimeRaw, tz)

        redScore = matchRed["score"]
        blueScore = matchBlue["score"]

        # used to create lists of data for the match as a whole and then for each alliance
        #    that is then used to extract the various elements
        matchBreakdown = match["score_breakdown"]
        matchRedBreakdown = matchBreakdown["red"]
        matchBlueBreakdown = matchBreakdown["blue"]

        redFouls = matchRedBreakdown["foulCount"]
        blueFouls = matchBlueBreakdown["foulCount"]

        redTechFouls = matchRedBreakdown["techFoulCount"]
        blueTechFouls = matchBlueBreakdown["techFoulCount"]

        redAutoPts = matchRedBreakdown["autoPoints"]
        blueAutoPts = matchBlueBreakdown["autoPoints"]

        redTelePts = matchRedBreakdown["teleopPoints"]
        blueTelePts = matchBlueBreakdown["teleopPoints"]

        # CS = ChargeStation
        redCSPts = matchRedBreakdown["endgamePoints"]
        blueCSPts = matchBlueBreakdown["endgamePoints"]

        # redLinksRP = matchRedBreakdown["???"]
        # blueLinksRP = matchBlueBreakdown["???"]
        
        # CSRP = Charge Station Ranking Point
        # redCSRP = matchRedBreakdown["???"]
        # blueCSRP = matchBlueBreakdown["???"]

        if match.comp_level == "qm":
            query = ("UPDATE BAmatchData "
                    f"SET actualTime = '{str(matchActTime)[11:16]}', "
                    f"redScore = {int(redScore)}, blueScore = {int(blueScore)}, "
                    f"redFouls = {int(redFouls)}, blueFouls = {int(blueFouls)}, "
                    f"redTechFouls = {int(redTechFouls)}, blueTechFouls = {int(blueTechFouls)}, "
                    f"redAutoPoints = {int(redAutoPts)}, blueAutoPoints = {int(blueAutoPts)}, "
                    f"redTelePoints = {int(redTelePts)}, blueTelePoints = {int(blueTelePts)}, "
                    f"redChargeStationPoints = {int(redCSPts)}, blueChargeStationPoints = {int(blueCSPts)} "
                    # f"redLinksRP = {int(redLinksRP)}, blueLinksRP = {int(blueLinksRP)}, "
                    # f"redChargeStationRP = {int(redCSRP)}, blueChargeStationRP = {int(blueCSRP)} "
                    f"WHERE matchNum = {matchNum}")
            print(f"Processing match number = {matchNum}")
            cursor.execute(query)
            conn.commit()

cursor.close()
conn.close()

print("Time: %0.2f seconds" % (time.time() - start_time))
print()
