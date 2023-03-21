import statistics

def teleObstructed(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 13
    numberOfMatchesPlayed = 0
    teleObstructedList = []
    
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
            Obstructed = matchResults[analysis.columns.index('teleObstructed')]
            
            if Obstructed == 0:
                teleObstructedColor = 1
            elif Obstructed <= 5:
                teleObstructedColor = 2
            elif Obstructed <= 10:
                teleObstructedColor = 3
            elif Obstructed <= 15:
                teleObstructedColor = 4
            elif Obstructed > 15:
                teleObstructedColor = 5
            else:
                Obstructed = "999"
                teleObstructedColor = 0

            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = str(Obstructed)
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = Obstructed
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleObstructedColor
            
            numberOfMatchesPlayed += 1
            teleObstructedList.append(Obstructed)

    if numberOfMatchesPlayed > 0:
        mean = round(statistics.mean(teleObstructedList), 1)
        median = round(statistics.median(teleObstructedList), 1)
        rsCEA['S1V'] = mean
        rsCEA['S1D'] = str(mean)
        rsCEA['S2V'] = median
        rsCEA['S2D'] = str(median)
    return rsCEA