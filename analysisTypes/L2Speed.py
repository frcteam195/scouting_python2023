import statistics

def speed(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 30 
    numberOfMatchesPlayed = 0

    category = 'speed'

    # Loop through each match the robot played in.
    for matchResults in rsRobotMatchData:
        rsCEA['team'] = matchResults[analysis.L2Columns.index('team')]
        rsCEA['eventID'] = matchResults[analysis.L2Columns.index('eventID')]
        preNoShow = matchResults[analysis.L2Columns.index('preNoShow')]
        scoutingStatus = matchResults[analysis.L2Columns.index('scoutingStatus')]
        if preNoShow == 1:
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'D'] = 'DNS'
        elif scoutingStatus == 2:
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'D'] = 'UR'
        else:
            categoryValue = matchResults[analysis.L2Columns.index(category)]
            if categoryValue is None:
                categoryValue = 0

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'D'] = matchResults[
                analysis.L2Columns.index(category)]
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'V'] = matchResults[
                analysis.L2Columns.index(category)]

    return rsCEA