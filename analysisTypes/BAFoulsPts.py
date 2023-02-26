import statistics

def BAFoulsPts(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 24
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    BAFoulsPtsList = []
    
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

            fouls *= 5
            techFouls *= 12

            if fouls is None:
                fouls = 0
            if techFouls is None:
                techFouls = 0

            totalFouls = fouls + techFouls

            BAFoulsPtsDisplay = totalFouls
            BAFoulsPtsValue = totalFouls

            if totalFouls <= 5:
                BAFoulsPtsColor = 5
            elif totalFouls <= 10:
                BAFoulsPtsColor = 4
            elif totalFouls <= 15:
                BAFoulsPtsColor = 3
            elif totalFouls <= 20:
                BAFoulsPtsColor = 2
            elif totalFouls > 20:
                BAFoulsPtsColor = 1
                       

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = BAFoulsPtsDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = BAFoulsPtsValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = BAFoulsPtsColor

            BAFoulsPtsList.append(BAFoulsPtsValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(BAFoulsPtsList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(BAFoulsPtsList), 1))
        rsCEA['S2V'] = round(statistics.median(BAFoulsPtsList), 1)
        rsCEA['S2D'] = str(round(statistics.median(BAFoulsPtsList), 1))
    return rsCEA