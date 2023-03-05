import statistics
#import mysql.connector
def postBrokeDown(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 18
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    postBrokeDownList = []
    
    # Loop through each match the robot played in.
    for matchResults in rsRobotMatchData:
        rsCEA['team'] = matchResults[analysis.columns.index('team')]
        rsCEA['eventID'] = matchResults[analysis.columns.index('eventID')]
        preNoShow = matchResults[analysis.columns.index('preNoShow')]
        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if preNoShow == 1:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'DNS'
        elif scoutingStatus == 2:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'UR'
        else:
            postBrokeDown = matchResults[analysis.columns.index('postBrokeDown')]
            
            if postBrokeDown is None:
                postBrokeDown = 0
                postBrokeDownDisplay = 999
            elif postBrokeDown == 0:
                postBrokeDownDisplay = 'N'
                postBrokeDownValue = 0
                postBrokeDownColor = 4
            else:
                postBrokeDownDisplay = 'Y'
                postBrokeDownColor = 2
                postBrokeDownValue = 1
                postBrokeDownColor = 2

            postBrokeDownList.append(postBrokeDownValue)

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postBrokeDownDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postBrokeDownValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postBrokeDownColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postBrokeDownList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(postBrokeDownList), 1))

    return rsCEA