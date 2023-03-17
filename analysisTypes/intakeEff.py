import statistics

def intakeEff(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 36
    category = 'intakeEff'
    count = 0
    numberOfMatchesPlayed = 0
    valueList = []

    for matchResults in rsRobotL2MatchData:
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
                categoryValue = 999
                categoryDisplay = '999'
                categoryFormat = 0
            elif categoryValue == 0:
                categoryDisplay = 'NA'
                categoryFormat = 0
                valueList.append(categoryValue)
            else:
                categoryDisplay = str(categoryValue)
                categoryFormat = categoryValue
                valueList.append(categoryValue)
                count += 1

            numberOfMatchesPlayed += 1
            
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'D'] = categoryDisplay
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'V'] = categoryValue
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'F'] = categoryFormat

    if numberOfMatchesPlayed > 0:
        if count > 0:
            rsCEA['S1V'] = round(statistics.mean(valueList), 1)
            rsCEA['S1D'] = str(round(statistics.mean(valueList), 1))
            rsCEA['S2V'] = round(statistics.median(valueList), 1)
            rsCEA['S2D'] = str(round(statistics.median(valueList), 1))
        else:
                rsCEA['S1V'] = 0
                rsCEA['S1D'] = '-'
                rsCEA['S2V'] = 0
                rsCEA['S2D'] = '-'
    
    return rsCEA