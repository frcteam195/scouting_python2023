import statistics

def autoGamePieces(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 3
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    autoGamePiecesList = []

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
            
            
            numGamePieces = 0
            score1 = matchResults[analysis.columns.index('autoScore1')]
            score2 = matchResults[analysis.columns.index('autoScore2')]
            score3 = matchResults[analysis.columns.index('autoScore3')]
            score4 = matchResults[analysis.columns.index('autoScore4')]

            if score1 > 0:
                numGamePieces += 1
            if score2 > 0:
                numGamePieces += 1
            if score3 > 0:
                numGamePieces += 1
            if score4 > 0:
                numGamePieces += 1

            autoDisplay = numGamePieces
            autoValue = numGamePieces

            if numGamePieces == 0:
                autoColor = 1
            elif numGamePieces == 1:
                autoColor = 2
            elif numGamePieces == 2:
                autoColor =3
            elif numGamePieces == 3:
                autoColor = 4
            elif numGamePieces > 3:
                autoColor = 5

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = autoDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = autoValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = autoColor

            autoGamePiecesList.append(autoValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(autoGamePiecesList), 1)
    return rsCEA