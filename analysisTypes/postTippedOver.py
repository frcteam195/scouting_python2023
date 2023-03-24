import statistics

def postTippedOver(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 22
    numberOfMatchesPlayed = 0
    postTippedOverList = []

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
            postTippedOver = matchResults[analysis.columns.index('postTippedOver')]  
            
            if postTippedOver is None:
                postTippedOverDisplay = '999'
                postTippedOverValue = 0
                postTippedOverColor = 1
            elif postTippedOver == 0:
                postTippedOverDisplay = 'N'
                postTippedOverValue = 1
                postTippedOverColor = 4
            else:
                postTippedOverDisplay = 'Y'
                postTippedOverValue = 0
                postTippedOverColor = 2
            
            postTippedOverList.append(postTippedOverValue)
            numberOfMatchesPlayed += 1

            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postTippedOverDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postTippedOverValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postTippedOverColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postTippedOverList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(postTippedOverList), 1))
    
    return rsCEA
