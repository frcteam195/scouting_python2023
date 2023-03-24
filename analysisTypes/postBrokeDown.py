import statistics
#import mysql.connector
def postBrokeDown(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 18
    numberOfMatchesPlayed = 0
    postBrokeDownList = []
    
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
                postBrokeDownDisplay = '999'
                postBrokeDownValue = 0
                postBrokeDownColor = 0
            elif postBrokeDown == 0:
                postBrokeDownDisplay = 'N'
                postBrokeDownValue = 1
                postBrokeDownColor = 4
            else:
                postBrokeDownDisplay = 'Y'
                postBrokeDownValue = 0
                postBrokeDownColor = 2

            postBrokeDownList.append(postBrokeDownValue)
            numberOfMatchesPlayed += 1

            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postBrokeDownDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postBrokeDownValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postBrokeDownColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postBrokeDownList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(postBrokeDownList), 1))

    return rsCEA