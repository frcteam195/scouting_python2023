import mysql.connector
import numpy as np
import os
import sys
import datetime
import time
import argparse
import configparser

# import all the analysis types listed in analysisTypes/__init__.py
# add each analysisType to the analysisTypeDict dictionary 
from analysisTypes import *
analysisTypesDict = {
                    "startingPosition": startingPosition.startingPosition,
                    "autoScore": autoScore.autoScore,
                    "autoGamePieces": autoGamePieces.autoGamePieces,
                    "autoRamp": autoRamp.autoRamp,
                    "teleHigh": teleHigh.teleHigh,
                    "teleMid": teleMid.teleMid,
                    "teleLow": teleLow.teleLow,
                    "teleTotal": teleTotal.teleTotal,
                    "teleCones": teleCones.teleCones,
                    "teleCubes": teleCubes.teleCubes,
                    "teleCommunity": teleCommunity.teleCommunity,
                    "teleLZPickup": teleLZPickup.teleLZPickup,
                    "teleObstructed": teleObstructed.teleObstructed,
                    "teleWasObstructed": teleWasObstructed.teleWasObstructed,
                    "ramp": ramp.ramp,
                    "rampPos": rampPos.rampPos,
                    "postSubBroke": postSubBroke.postSubBroke,
                    "postBrokeDown": postBrokeDown.postBrokeDown,
                    # "postReorientCone": postReorientCone.postReorientCone,
                    "postShelfPickup": postShelfPickup.postShelfPickup,
                    "postGroundPickup": postGroundPickup.postGroundPickup,
                    "postTippedOver": postTippedOver.postTippedOver,
                    "matchVideos": matchVideos.matchVideos,
                    "BAFoulsPts": BAFoulsPts.BAFoulsPts,
                    "BARankingPoints": BARankingPoints.BARankingPoints,
                    "totalScore": totalScore.totalScore,
                    "teleScore": teleScore.teleScore,
                    "graphicTeleInfo": graphicTeleInfo.graphicTeleInfo,
                    "graphicStartPos": graphicStartPos.graphicStartPos,
                    "autoScorePosHigh": autoScorePosHigh.autoScorePosHigh,
                    "autoScorePosMid": autoScorePosMid.autoScorePosMid,
                    "autoScorePosLow": autoScorePosLow.autoScorePosLow,
                    "speed": speed.speed,
                    # "sturdiness": sturdiness.sturdiness,
                    "climb": climb.climb,
                    "scoringEff": scoringEff.scoringEff,
                    "intakeEff": intakeEff.intakeEff,
                    "goodOffBot": goodOffBot.goodOffBot,
                    "goodDefBot": goodDefBot.goodDefBot,
                    "rampTime": rampTime.rampTime
                    } 

# parser to choose the database where the table will be written
parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host

CEA_tmpTable = "CEanalysisTmp"
BAoprTable = "BAoprs"
BArankTable = "BAranks"

# Read the configuration file
config = configparser.ConfigParser()
config.read('helpers/config.ini')

# Get the database login information from the configuration (ini) file
host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']


# Define a Class called analysis
class analysis():
    # Inside the class there are several functions defined:
    #   _scoutingDBconnector = sets up the database connection and creates the cursor for running SQL queries
    #       _run_query = runs a generic query based on string passed to the functon. Used by several other functions
    #   _createCEanalysisTmp = drops (if exists) and builds tmp file for Current Event Analysis data
    #   _setColumns = retrieves the column headings from the database table so we don't need to hardcode them  
    #   _getTeams = gets the team list and sets the results to rsRobots
    #   _getTeamData =  retrieves data records for a given team, for all their matches, and sets the results to rsRobotMatchData
    #   _analyzeTeams = loops over teams and then loops over all analysisTypes setting the results of each inner loop to rsCEA
    #       _insertAnalysis = inserts the rsCEA records into the CEanalysisTmp table, used within _analyzeTeams
    #   _rankTeamsAll = loops over all analysisTypeIDs that are slated for ranking and calls the _rankTeamsSingle function
    #       _rankTeamsSingle = ranks teams based on S1V for a given analysisTypeID using numpy
    #   _renameTable = renames CEA_tmpTable to CEanalysis

    def __init__(self):
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        start_time = time.time()
        print("this script takes a while, please be patient!")

        self._scoutingDBconnector()
        self._createCEanalysisTmp()
        self.columns = []
        self.L2Columns = []
        self.pitColumns = []
        self.rsRobots = self._getTeams()
        self._analyzeTeams()
        self._rankTeamsAll()
        self._renameTable()

        print("Time: %0.2f seconds" % (time.time() - start_time))

    # Connect to database and setup cursor
    def _scoutingDBconnector(self):
        self.conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
        self.cursor = self.conn.cursor()
    
    # Function to run a query - the query string must be passed to the function
    def _run_query(self, query):
        self.cursor.execute(query)
        
    # Function to drop existing CEanalysisTmp table if it exists (it should not) and rebuild table
    def _createCEanalysisTmp(self):
        self._run_query("DROP TABLE IF EXISTS CEanalysisTmp")
        try:
            SQLfile = open('CEanalysisTmp.sql','r')
        except IOError:
            print("CEanalysisTmp file could not be opened, aborting!")
            sys.exit(1)
        query = SQLfile.read()
        self._run_query(query)

    # Function to determine the DB table column headers
    def _setColumns(self, columns):
        self.columns = columns
    
    def _setL2Columns(self, L2Columns):
        self.L2Columns = L2Columns

    def _setPitColumns(self, pitColumns):
        self.pitColumns = pitColumns

    # Function to get the team list and set it to rsRobots. Uses the _run_query function defined above.
    def _getTeams(self):
        query = "SELECT matchScouting.team FROM (matchScouting " + \
                "INNER JOIN matches ON matchScouting.matchID = matches.matchID) " + \
                "INNER JOIN events ON matches.eventID = events.eventID " + \
                "WHERE (((events.currentEvent) = 1)) " + \
                "GROUP BY CAST(matchScouting.team AS INT), matchScouting.team " + \
                "HAVING (((matchScouting.team) Is Not Null))"
        self._run_query(query)
        rsRobots = self.cursor.fetchall()
        assert len(rsRobots) > 0, "No robots found"   # assert exits with "no robots found" or returns team list
        return rsRobots
    

    # Function to retrieve L1 data records for a given team for all their matches and set it to rsRobotMatchData
    def _getTeamData(self, team):
        query = "SELECT matchScouting.*, matches.matchNum " + \
                "FROM (events INNER JOIN matches ON events.eventID = matches.eventID) " + \
                "INNER JOIN matchScouting ON (matches.eventID = matchScouting.eventID) " + \
                "AND (matches.matchID = matchScouting.matchID) " + \
                "INNER JOIN teams ON (matchScouting.team = teams.team) " + \
                "WHERE (((matchScouting.team) = " + team[0] + " AND ((events.currentEvent) = 1)) " + \
                "AND ((scoutingStatus = 1) OR (scoutingStatus = 2) OR (scoutingStatus = 3)) " + \
                "AND (matchScouting.teamMatchNum <= 12)) " + \
                "ORDER BY matchScouting.teamMatchNum"
        self._run_query(query)
        self._setColumns([column[0] for column in list(self.cursor.description)])
        rsRobotMatchData = self.cursor.fetchall()
        if rsRobotMatchData:
            return rsRobotMatchData
        else:
            return None
    
    # Function to retrieve L2 data records for a given team for all their matches and set it to rsRobotMatchData
    def _getL2TeamData(self, team):
        query = "SELECT matchScoutingL2.*, matches.matchNum " + \
                "FROM (events INNER JOIN matches ON events.eventID = matches.eventID) " + \
                "INNER JOIN matchScoutingL2 ON (matches.eventID = matchScoutingL2.eventID) " + \
                "AND (matches.matchID = matchScoutingL2.matchID) " + \
                "INNER JOIN teams ON (matchScoutingL2.team = teams.team) " + \
                "WHERE (((matchScoutingL2.team) = " + team[0] + " AND ((events.currentEvent) = 1)) " + \
                "AND ((scoutingStatus = 1) OR (scoutingStatus = 2) OR (scoutingStatus = 3)) " + \
                "AND (matchScoutingL2.teamMatchNum <= 12)) " + \
                "ORDER BY matchScoutingL2.teamMatchNum"
        self._run_query(query)
        self._setL2Columns([L2column[0] for L2column in list(self.cursor.description)])
        rsRobotL2MatchData = self.cursor.fetchall()
        # print(rsRobotL2MatchData)
        if rsRobotL2MatchData:
            return rsRobotL2MatchData
        else: 
            rsRobotL2MatchData = 0
            return rsRobotL2MatchData

    # Function to retrieve pit data records for a given team
    def _getPitData(self, team):
        query = f"SELECT pit.* FROM pit JOIN events ON pit.eventID = events.eventID WHERE pit.team = {team[0]} AND events.currentEvent = 1"
        self._run_query(query)
        self._setPitColumns([pitColumn[0] for pitColumn in list(self.cursor.description)])
        rsRobotPitData = self.cursor.fetchall()
        if rsRobotPitData:
            return rsRobotPitData
        else:
            rsRobotPitData = 0
            return rsRobotPitData
    
    # runs each of the analysisTypes and outputs the results to rsCEA
    def _analyzeTeams(self):
        for team in self.rsRobots:
            # analysisTypesDict defined at top of script
            for analysisType2analyze in analysisTypesDict:
                # print(f"analyzing team {team} using {analysisType2analyze}")
                rsRobotMatchData = self._getTeamData(team)
                rsRobotL2MatchData = self._getL2TeamData(team)
                rsRobotPitData = self._getPitData(team)
                teamName = str(team)
                teamName = teamName.translate(str.maketrans("", "", " ,()'"))
                if rsRobotMatchData:
                    rsCEA = analysisTypesDict[analysisType2analyze](analysis=self, rsRobotMatchData=rsRobotMatchData, rsRobotL2MatchData=rsRobotL2MatchData, rsRobotPitData=rsRobotPitData)
                    self._insertAnalysis(rsCEA)
                    self.conn.commit()
            # add one last analysisType to add BAoprs and BAranks to analysisTypeID = 80
            query = (f"INSERT INTO {CEA_tmpTable} (team, eventID, S1V, S1D, S2V, S2D, analysisTypeID) "
                     f"SELECT {BArankTable}.team, {BArankTable}.eventID, "
                     f"{BAoprTable}.OPR, {BAoprTable}.OPR, {BArankTable}.rank, {BArankTable}.rank, 80 "
                     f"FROM {BArankTable} "
                     f"INNER JOIN {BAoprTable} ON {BArankTable}.team = {BAoprTable}.team "
                     f"WHERE {BArankTable}.team = {teamName}")
            self._run_query(query)
    
     # Function to insert an rsCEA record into the DB.
    def _insertAnalysis(self, rsCEA):
        rsCEA_records = rsCEA.items()
        columnHeadings = str(tuple([record[0] for record in rsCEA_records])).replace("'", "")
        values = str(tuple([record[1] for record in rsCEA_records]))
        query = "INSERT INTO " + CEA_tmpTable + " " + columnHeadings + " VALUES " + values
        self._run_query(query)
        self.conn.commit()

    # Function to retrieve S1V values for a given analysisType and use numpy to determine percentiles
    def _rankTeamsSingle(self, analysis_type):
        query = "SELECT team, S1V FROM " + CEA_tmpTable + " WHERE analysisTypeID = " + str(analysis_type)
        self._run_query(query)
        team_sum1 = self.cursor.fetchall() # List of tuples (team, S1V)
        # print(team_sum1)
        if len(team_sum1) > 0:
            team_sum1 = [team_tup for team_tup in team_sum1 if team_tup[1] is not None]
            sum1 = [item[1] for item in team_sum1]
            percentiles = np.percentile(sum1, [25, 50, 75, 90])

            # team_coloring = {}
            for team in team_sum1:
                if team[1] <= percentiles[0]:
                    team_color = 1
                    team_display = 10
                elif team[1] <= percentiles[1]:
                    team_color = 2
                    team_display = 25
                elif team[1] <= percentiles[2]:
                    team_color = 3
                    team_display = 50
                elif team[1] <= percentiles[3]:
                    team_color = 4
                    team_display = 75
                else:
                    team_color = 5
                    team_display = 90

                query = "UPDATE " + CEA_tmpTable + " SET " + CEA_tmpTable + ".S3F = " \
                        + str(team_color) + ", " + CEA_tmpTable + ".S3D = "\
                        + str(team_display) + ", " + CEA_tmpTable + ".S3V = " + str(team_display) \
                        + " WHERE " + CEA_tmpTable + ".team = '" + str(team[0]) \
                        + "' AND " + CEA_tmpTable + ".analysisTypeID = " + str(analysis_type)
                self._run_query(query)
                self.conn.commit()
        else:
            print(f"Ranking data was not found in the db for analysisTypeID = {analysis_type}")

    # run the _rankTeamsSingle for all analysis types in the analysisTypeList defined in this function
    def _rankTeamsAll(self):
        query = "SELECT analysisTypeID FROM analysisTypes WHERE runRank = 1"
        self._run_query(query)
        analysisTypeList = self.cursor.fetchall()
        for analysisType in analysisTypeList:
            analysisType = str(analysisType)
            analysisType = analysisType.translate(str.maketrans("", "", " ,()'"))
            self._rankTeamsSingle(analysisType)

    def _renameTable(self):
        query = "DELETE FROM CEanalysis WHERE eventID = (SELECT eventID FROM events WHERE currentEvent = 1)"
        self._run_query(query)
        query = ("INSERT INTO CEanalysis SELECT * FROM " + CEA_tmpTable)
        self._run_query(query)
        self.conn.commit()

# This initizlzes the analysis Class and thus runs the program.
if __name__ == '__main__':
    myAnalysis = analysis()
