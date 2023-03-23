import statistics

def BAFoulsPts(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 24
    numberOfMatchesPlayed = 0
    foulPtsList = []
    
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
            
            fouls = matchResults[analysis.columns.index('BAfouls')]
            techFouls = matchResults[analysis.columns.index('BAtechFouls')]

            if fouls is None:
                fouls = 0
            if techFouls is None:
                techFouls = 0

            foulPts = fouls * 5
            techFoulPts = techFouls * 12
            
            totalFoulPts = foulPts + techFoulPts

            foulPtsDisplay = (totalFoulPts * -1)
            foulPtsValue = totalFoulPts

            if totalFoulPts >= -5:
                foulPtsColor = 5
            elif totalFoulPts >= -10:
                foulPtsColor = 4
            elif totalFoulPts >= -15:
                foulPtsColor = 3
            elif totalFoulPts >= -20:
                foulPtsColor = 2
            elif totalFoulPts < -20:
                foulPtsColor = 1
                       
            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = foulPtsDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = foulPtsValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = foulPtsColor

            foulPtsList.append(foulPtsValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(foulPtsList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(foulPtsList), 1))
        rsCEA['S2V'] = round(statistics.median(foulPtsList), 1)
        rsCEA['S2D'] = str(round(statistics.median(foulPtsList), 1))
    return rsCEA