import statistics

def BAFoulsPts(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 24
    numberOfMatchesPlayed = 0
    foulPtsList = []
    foulPtsRankingList = []
    
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
            fouls = matchResults[analysis.columns.index('BAfouls')]
            techFouls = matchResults[analysis.columns.index('BAtechFouls')]

            if fouls is None:
                fouls = 0
            if techFouls is None:
                techFouls = 0

            foulPts = ((fouls * 5) + (techFouls * 12))
            rankingValue = foulPts * -1

            if foulPts <= 0:
                foulPtsColor = 5
            elif foulPts <= 5:
                foulPtsColor = 4
            elif foulPts <= 10:
                foulPtsColor = 3
            elif foulPts <= 15:
                foulPtsColor = 2
            elif foulPts > 15:
                foulPtsColor = 1
                       
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = str(foulPts)
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = foulPts
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = foulPtsColor

            foulPtsList.append(foulPts)
            foulPtsRankingList.append(rankingValue)
            numberOfMatchesPlayed += 1

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(foulPtsRankingList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(foulPtsList), 1))
        rsCEA['S2V'] = round(statistics.median(foulPtsRankingList), 1)
        rsCEA['S2D'] = str(round(statistics.median(foulPtsList), 1))

    return rsCEA