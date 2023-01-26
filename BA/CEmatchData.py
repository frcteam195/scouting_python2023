import mysql.connector
import tbapy
import argparse
import datetime as dt
import time
import pytz
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

# get the BAeventID and timezone for the current event
cursor.execute("SELECT events.BAeventID FROM events WHERE events.currentEvent = 1;")
currentEvent = cursor.fetchone()[0]
cursor.execute("SELECT events.timeZone FROM events WHERE events.currentEvent = 1;")
timeZone = cursor.fetchone()[0]

qNum = 0
eventInfo = tba.event_matches(currentEvent)
tz = pytz.timezone(str(timeZone))
print(type(tz))

for match in eventInfo:
    # print(match)
    print("be patient, lots of data to grab from TBA")
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
        query = "INSERT INTO BAmatchData (matchNumber, matchTime, red1, red2, red3, blue1, blue2, blue3) " + \
                f"VALUES ({matchNum}, '{str(matchTime)[11:16]}', {int(str(matchRedTeams[0])[3:])}, {int(str(matchRedTeams[1])[3:])}, {int(str(matchRedTeams[2])[3:])}, {int(str(matchBlueTeams[0])[3:])}, {int(str(matchBlueTeams[1])[3:])}, {int(str(matchBlueTeams[2])[3:])})"
        print(query)
        # cursor.execute(query)
        # conn.commit()
'''
    if matchInfo.actual_time is not None:
        matchActTime = dt.datetime.fromtimestamp(matchActTimeRaw, tz)

        matchRedScore = matchRed["score"]
        matchBlueScore = matchBlue["score"]

        matchBreakdown = match["score_breakdown"]
        matchRedBreakdown = matchBreakdown["red"]
        matchBlueBreakdown = matchBreakdown["blue"]

        matchRedFouls = matchRedBreakdown["foulCount"]
        matchBlueFouls = matchBlueBreakdown["foulCount"]

        matchRedTechFouls = matchRedBreakdown["techFoulCount"]
        matchBlueTechFouls = matchBlueBreakdown["techFoulCount"]

        matchRedAutoPoints = matchRedBreakdown["autoPoints"]
        matchBlueAutoPoints = matchBlueBreakdown["autoPoints"]

        matchRedTelePoints = matchRedBreakdown["teleopPoints"]
        matchBlueTelePoints = matchBlueBreakdown["teleopPoints"]

        matchRedHangarPoints = matchRedBreakdown["endgamePoints"]
        matchBlueHangarPoints = matchBlueBreakdown["endgamePoints"]

        matchRedRankingPoints = matchRedBreakdown["cargoBonusRankingPoint"]
        matchBlueRankingPoints = matchBlueBreakdown["cargoBonusRankingPoint"]

        matchRedHangarRP = matchRedBreakdown["hangarBonusRankingPoint"]
        matchBlueHangarRP = matchBlueBreakdown["hangarBonusRankingPoint"]

        #print(str(matchTime) + "\n")

        if match.comp_level == "qm":
            #cursor.execute("INSERT INTO BlueAllianceMatchData(MatchNumber, MatchTime, ActualTime, Red1, Red2, Red3, Blue1, Blue2, Blue3, RedScore, BlueScore, "
            #                "RedFouls, BlueFouls, RedTechFouls, BlueTechFouls, RedAutoPoints, BlueAutoPoints, RedTelePoints, BlueTelePoints, "
            #                "RedHangerPoints, BlueHangerPoints, RedCargoRanking, BlueCargoRanking, RedHangarRanking, BlueHangarRanking) "
            #                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", \
            #                (matchNum, str(matchTime)[11:16], str(matchActTime)[11:16], int(str(matchRedTeams[0])[3:]), int(str(matchRedTeams[1])[3:]), int(str(matchRedTeams[2])[3:]), int(str(matchBlueTeams[0])[3:]), int(str(matchBlueTeams[1])[3:]), int(str(matchBlueTeams[2])[3:]), \
            #                int(matchRedScore), int(matchBlueScore), int(matchRedFouls), int(matchBlueFouls), int(matchRedTechFouls), int(matchBlueTechFouls), \
            #                int(matchRedAutoPoints), int(matchBlueAutoPoints), int(matchRedTelePoints), int(matchBlueTelePoints), int(matchRedHangarPoints), int(matchBlueHangarPoints), \
            #                int(matchRedRankingPoints), int(matchBlueRankingPoints), bool(matchRedHangarRP), bool(matchBlueHangarRP)))

            cursor.execute("UPDATE BlueAllianceMatchData "
                            f"SET ActualTime = '{str(matchActTime)[11:16]}', RedScore = {int(matchRedScore)}, BlueScore = {int(matchBlueScore)}, "
                            f"RedFouls = {int(matchRedFouls)}, BlueFouls = {int(matchBlueFouls)}, RedTechFouls = {int(matchRedTechFouls)}, BlueTechFouls = {int(matchBlueTechFouls)}, "
                            f"RedAutoPoints = {int(matchRedAutoPoints)}, BlueAutoPoints = {int(matchBlueAutoPoints)}, RedTelePoints = {int(matchRedTelePoints)}, BlueTelePoints = {int(matchBlueTelePoints)}, "
                            f"RedHangerPoints = {int(matchRedHangarPoints)}, BlueHangerPoints = {int(matchBlueHangarPoints)}, RedCargoRanking = {int(matchRedRankingPoints)}, BlueCargoRanking = {int(matchBlueRankingPoints)}, "
                            f"RedHangarRanking = {bool(matchRedHangarRP)}, BlueHangarRanking = {bool(matchBlueHangarRP)} "
                            f"WHERE MatchNumber = {matchNum}")

            conn.commit()

print("Time: %0.2f seconds" % (time.time() - start_time))
print()


#eventInfoSorted = [(k[3:], eventInfo[k]) for k in sorted(eventInfo, key=eventInfo.get, reverse=True)]
# print(eventOPRSorted)

#for team in eventInfo:
    #query = "INSERT INTO BlueAllianceOPR (Team, OPR) VALUES " + "('" + str(team[0]) + "', '" + \
            #str(team[1]) + "');"
    # print(query)
    #cursor.execute(query)
    #conn.commit()
    #print(team)
#print('Writing OPRs to database')
'''