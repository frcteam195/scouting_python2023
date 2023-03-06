import statistics
#import mysql.connector
def postSubBroke(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 17
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    postSubBrokeList = []
    
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
            
            postSubBroke = matchResults[analysis.columns.index('postSubsystemBroke')]
            
            if postSubBroke is None:
                postSubBrokeDisplay = 999
                postSubBrokeValue = 999
            elif postSubBroke == 0:
                postSubBrokeDisplay = 'N'
                postSubBrokeValue = 0
                postSubBrokeColor = 4
            else:
                postSubBrokeDisplay = 'Y'
                postSubBrokeValue = 1
                postSubBrokeColor = 2
            
            postSubBrokeList.append(postSubBrokeValue)

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postSubBrokeDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postSubBrokeValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postSubBrokeColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postSubBrokeList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(postSubBrokeList), 1))

    return rsCEA
