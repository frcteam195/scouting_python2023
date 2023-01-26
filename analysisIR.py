import mysql.connector
import numpy as np
import os
import sys
import datetime
import time
import argparse
import configparser

# For each analysisType we create add a new import statement. We could import all analysisTypes
from analysisTypes.startingPosition import startingPosition  #1

# parser to choose the database where the table will be written
parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host

CEA_table = "CEanalysisTmp"
BAO_table = "BAoprs"
BAR_table = "BAranks"
MS_table = "BAmatchScouting"

# Read the configuration file
config = configparser.ConfigParser()
config.read('helpers/config.ini')

# Get the database login information from the configuration (ini) file
host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']
#print(host + " " + user + " " + passwd + " " + database)


# Define a Class called analysis
class analysis():
    # Inside the class there are several functions defined:
    #   _run_query = runs a query based on string passed to the functon
    #   _setColumns = retrieves the column headings from the database table so we don't need to hardcode them
    #   _wipeCEA = wipes away the CEanalysisTmp table
    #   _getTeams = gets the team list and sets the results to the rsRobots
    #   _getTeamData =  retrieves data records for a given team, for all their matches, and sets the results to rsRobotMatches
    #   _analyzeTeams = loops over teams and then loops over all analysisTypes setting the results of each inner loop to rsCEA
    #   _insertAnalysis = inserts the rsCEA records into the CEanalysisTmp table
    #   Those functions will not get called automatically
    #   so in order to get them to run we create a __init__ function which is a special function in Python
    #   that gets run every time the class is initialized. Here we build the DB connection cursor from within
    #   the __init__ function and then call the cursor, columns, wipeCEA, rsRobots, and analyzeTeams functions
    #   from within the __init__ function, which means they will be run automatically when the Class is initialized
    def __init__(self):
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        start_time = time.time()

        self.conn = mysql.connector.connect(user=user, passwd=passwd, host=host, database=database)
        self.cursor = self.conn.cursor()
        
        self._createCEanalysisTmp()
        self.columns = []
        self._wipeCEanalysisTmp()
        self.rsRobots = self._getTeams()
        self._analyzeTeams()
        # self._rankTeamsAll()
        # self._renameTable()

        print("Time: %0.2f seconds" % (time.time() - start_time))
        print()

    # Function to run a query - the query string must be passed to the function
    def _run_query(self, query):
        self.cursor.execute(query)

    # Function to determine the DB table column headers
    def _setColumns(self, columns):
        self.columns = columns

    # Function to wipe the CEA table. We may want to make this only remove CurrentEvent records.
    def _wipeCEanalysisTmp(self):
        self._run_query("DELETE FROM " + CEA_table + ";")
        self.conn.commit()

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

    def _renameTable(self):
        self._run_query("DROP TABLE CEanalysis;")
        self._run_query("ALTER TABLE " + CEA_table + " RENAME CEanalysis;")
        self.conn.commit()

    # Function to get the team list and set it to rsRobots. Uses the _run_query function defined above.
    #   The assert statement will return rsRobots if the record length > 0 and will exit with the
    #       message "No robots founds" if the record length is 0.
    def _getTeams(self):
        self._run_query("SELECT matchScouting.team FROM (matchScouting "
                       "INNER JOIN matches ON matchScouting.matchID = matches.matchID) "
                       "INNER JOIN events ON matches.eventID = events.eventID "
                       "WHERE (((events.currentEvent) = 1)) "
                       "GROUP BY CAST(matchScouting.team AS INT), matchScouting.team "
                       "HAVING (((matchScouting.team) Is Not Null))")
        rsRobots = self.cursor.fetchall()
        # print(rsRobots)
        assert len(rsRobots) > 0, "No robots found"
        return rsRobots

    # Function to retrieve data records for a given team for all their matches and set it to rsRobotMatches
    def _getTeamData(self, team):
        self._run_query("SELECT matchScouting.*, matches.matchNum "
            "FROM (events INNER JOIN matches ON events.eventID = matches.eventID) "
            "INNER JOIN matchScouting ON (matches.eventID = matchScouting.eventID) "
            "AND (matches.matchID = matchScouting.matchID) "
            "INNER JOIN teams ON (matchScouting.team = teams.team) "
            "WHERE (((matchScouting.team) = " + team[0] + " "
            "AND ((events.currentEvent) = 1))"
            "AND ((scoutingStatus = 1) OR (scoutingStatus = 2) OR (scoutingStatus = 3)) "
            "AND (matchScouting.teamMatchNum <= 12)) "
            "ORDER BY matchScouting.teamMatchNum")

        # Set columns to be a list of column headings in the Query results
        # Very cool - cursor.description is used to auto-determine the column headings in the matchScouting table
        #   so these values do not need to be hard-coded
        self._setColumns([column[0] for column in list(self.cursor.description)])

        rsRobotMatches = self.cursor.fetchall()
        # print(rsRobotMatches)

        # If rsRobotMatches is not zero length return rsRobotMatches otherwise return None. This allows the
        #   function to skip a robot analysis if that robot does not have any match records yet.
        if rsRobotMatches:
            return rsRobotMatches
        else:
            return None

    #
    def _analyzeTeams(self):
        # Loop over the # of teams and run each of the analysis functions calling _insertAnalysis after each one is run
        for team in self.rsRobots:
            rsRobotMatches = self._getTeamData(team)
            teamName = str(team)
            teamName = teamName.replace("('", "")
            teamName = teamName.replace("',)", "")
            # print(rsRobotMatches)

            if rsRobotMatches:
                rsCEA = startingPosition(analysis=self, rsRobotMatches=rsRobotMatches)
                self._insertAnalysis(rsCEA)
                self.conn.commit()


    # Helper function to rank a single analysis type, called by _rankTeamsAll
    def _rankTeamsSingle(self, analysis_type):
        # Get Summary 1 value for each team from CEA with analysis_type
        # Sort in descending order by sum 1 value
        # Determine percentile of each team
        # Optional: see if at percentile cutoffs there is any repeated values
        # Update summary 3 value in CEA for each team (rank based on percentile)
        self._run_query("SELECT Team, Summary1Value "
                        "FROM " + CEA_table + " "
                        "WHERE AnalysisTypeID = " + str(analysis_type) + ";")
        team_sum1 = self.cursor.fetchall() # List of tuples (team, summary1value)
        if len(team_sum1) > 0:
            team_sum1 = [team_tup for team_tup in team_sum1 if team_tup[1] is not None]
            # print(team_sum1)
            sum1 = [item[1] for item in team_sum1]
            percentiles = np.percentile(sum1, [25, 50, 75, 90])

            team_coloring = {}
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

                query = "UPDATE " + CEA_table + " SET " + CEA_table + ".Summary3Format = " \
                        + str(team_color) + ", " + CEA_table + ".Summary3Display = "\
                        + str(team_display) + ", " + CEA_table + ".Summary3Value = " + str(team_display) \
                        + " WHERE " + CEA_table + ".Team = '" + str(team[0]) \
                        + "' AND " + CEA_table + ".AnalysisTypeID = " + str(analysis_type) + " ;"
                #print(query);
                self._run_query(query)
                self.conn.commit()
        else:
            print('Ranking data was not found in the db')

    # run the _rankTeamsSingle for all analysis types in the analysisTypeList defined in this function
    def _rankTeamsAll(self):
        analysisTypeList=[10, 11, 20, 21, 22, 30, 60, 61, 62]
        for analysisType in analysisTypeList:
            # print(analysisType)
            self._rankTeamsSingle(analysisType)


    # Function to insert an rsCEA record into the DB.
    def _insertAnalysis(self, rsCEA):
        rsCEA_records = rsCEA.items()
        print(rsCEA)
        # Get the columnHeadings and values, do some formatting, and then use the _run_query function to run the
        #   query and the conn.commit to insert into the DB.
        columnHeadings = str(tuple([record[0] for record in rsCEA_records])).replace("'", "")
        values = str(tuple([record[1] for record in rsCEA_records]))
        print(values)

        # Insert the records into the DB
        self._run_query("INSERT INTO " + CEA_table + " "
                        + columnHeadings + " VALUES "
                        + values + ";")
        # print(columnHeadings + values)
        self.conn.commit()


# This initizlzes the analysis Class and thus runs the program.
if __name__ == '__main__':
    myAnalysis = analysis()
    
