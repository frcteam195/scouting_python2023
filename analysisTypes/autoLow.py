import statistics

def autoLowPieces(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 50
    numberOfMatchesPlayed = 0
    autoPieceList = []
    
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
            scorePos1 = matchResults[analysis.columns.index('autoScore1')]
            scorePos2 = matchResults[analysis.columns.index('autoScore2')]
            scorePos3 = matchResults[analysis.columns.index('autoScore3')]
            scorePos4 = matchResults[analysis.columns.index('autoScore4')]
            
            totalPieces = 0
            if (scorePos1 >= 19) and (scorePos1 <= 27):
                totalPieces += 1
            if (scorePos2 >= 19) and (scorePos2 <= 27):
                totalPieces += 1
            if (scorePos3 >= 19) and (scorePos3 <= 27):
                totalPieces += 1
            if (scorePos4 >= 19) and (scorePos4 <= 27):
                totalPieces += 1
            autoPieceList.append(totalPieces)

            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = str(totalPieces)
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = totalPieces

    if numberOfMatchesPlayed > 0:
        mean = round(statistics.mean(autoPieceList), 1)
        median = round(statistics.median(autoPieceList), 1)
        rsCEA['S1V'] = mean
        rsCEA['S1D'] = str(mean)
        rsCEA['S2V'] = median
        rsCEA['S2D'] = str(median)
        rsCEA['S4V'] = statistics.stdev(autoPieceList)
        
    return rsCEA