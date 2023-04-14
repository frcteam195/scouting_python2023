import statistics
def BARankingPoints(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 25
    numberOfMatchesPlayed = 0
    BARankingPointsList = []
    
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
            linkRP = matchResults[analysis.columns.index('BAlinkRP')]
            chargeStationRP = matchResults[analysis.columns.index('BAchargeStationRP')]

            if linkRP is None:
                linkRP = 0
            if chargeStationRP is None:
                chargeStationRP = 0

            if linkRP == 0 and chargeStationRP == 0:
                display = '0|0'
                color = 1
                rankingPoints = 0
                BARankingPointsList.append(rankingPoints)
            elif linkRP == 0 and chargeStationRP == 1:
                display = '0|1'
                color = 3
                rankingPoints = 1
                BARankingPointsList.append(rankingPoints)
            elif linkRP == 1 and chargeStationRP == 0:
                display = '1|0'
                color = 4
                rankingPoints = 1
                BARankingPointsList.append(rankingPoints)
            elif linkRP == 1 and chargeStationRP == 1:
                display = '1|1'
                color = 5
                rankingPoints = 2
                BARankingPointsList.append(rankingPoints)
            else:
                display = '999'
                color = 2
                rankingPoints = 0
                BARankingPointsList.append(rankingPoints)

            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = str(display)
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = rankingPoints
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = color

            numberOfMatchesPlayed += 1

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(BARankingPointsList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(BARankingPointsList), 1))
        rsCEA['S2V'] = round(statistics.median(BARankingPointsList), 1)
        rsCEA['S2D'] = str(round(statistics.median(BARankingPointsList), 1))
        
    return rsCEA