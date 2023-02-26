import statistics
#import mysql.connector
def BARankingPoints(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 25
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    BARankingPointsList = []
    
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
            
            linkRP = matchResults[analysis.columns.index('BAlinkRP')]
            chargeStationRP = matchResults[analysis.columns.index('BAchargeStationRP')]

            if linkRP is None:
                linkRP = 0
            if chargeStationRP is None:
                chargeStationRP = 0

            totalRP = linkRP + chargeStationRP

            BARankingPointsDisplay = str(linkRP) + "|" + str(chargeStationRP)
            BARankingPointsValue = totalRP
                       
            if totalRP == 0:
                BARankingPointsColor = 2
            elif totalRP == 1:
                BARankingPointsColor = 3
            elif totalRP == 2:
                BARankingPointsColor = 4    

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = BARankingPointsDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = BARankingPointsValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = BARankingPointsColor

            BARankingPointsList.append(BARankingPointsValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(BARankingPointsList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(BARankingPointsList), 1))
        rsCEA['S2V'] = round(statistics.median(BARankingPointsList), 1)
        rsCEA['S2D'] = str(round(statistics.median(BARankingPointsList), 1))
    return rsCEA