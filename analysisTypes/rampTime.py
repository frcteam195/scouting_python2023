import statistics
#import mysql.connector
def rampTime(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 28
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    rampTimeList = []
    
    # Loop through each match the robot played in.
    for matchResults in rsRobotMatchData:
        rsCEA['team'] = matchResults[analysis.columns.index('team')]
        rsCEA['eventID'] = matchResults[analysis.columns.index('eventID')]
        # We are hijacking the starting position to write DNS or UR. This should go to Auto as it will not
        #   likely be displayed on team picker pages.
        preNoShow = matchResults[analysis.columns.index('preNoShow')]
        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if preNoShow == 1:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'DNS'
        elif scoutingStatus == 2:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'UR'
        else:
            
            rampTime = matchResults[analysis.columns.index('rampStartTime')]
            
            if rampTime is None:
                rampTime = 0
           

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = rampTime
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = rampTime
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = 0

            rampTimeList.append(rampTime)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(rampTimeList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(rampTimeList), 1))
        rsCEA['S2V'] = round(statistics.median(rampTimeList), 1)
        rsCEA['S2D'] = str(round(statistics.median(rampTimeList), 1))
    return rsCEA