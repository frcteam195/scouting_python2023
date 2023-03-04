import statistics

def startingPosition(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 1 
    numberOfMatchesPlayed = 0

    # example for loading pit data into analysis
    # if rsRobotPitData == 0:
    #   # print("doing nothing")
    # else: 
    #     for pitResults in rsRobotPitData:
    #         width = pitResults[analysis.pitColumns.index('width')]

     # example for loading L2 data into analysis
    # if rsRobotL2MatchData == 0:
    #     #nprint("doing nothing")
    # else: 
    #     for L2Results in rsRobotL2MatchData:
    #         print(rsRobotL2MatchData)

    # Loop through each match the robot played in.
    for matchResults in rsRobotMatchData:
        rsCEA['team'] = matchResults[analysis.columns.index('team')]
        rsCEA['eventID'] = matchResults[analysis.columns.index('eventID')]

        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if scoutingStatus == 1:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'DNS'
        elif scoutingStatus == 2:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'UR'
        else:
            preStartPos = matchResults[analysis.columns.index('preStartPos')]
            if preStartPos is None:
                preStartPos = 0

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = matchResults[
                analysis.columns.index('preStartPos')]
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = matchResults[
                analysis.columns.index('preStartPos')]

    return rsCEA