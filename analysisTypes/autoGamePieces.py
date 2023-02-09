import statistics

def autoGamePieces(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 3
    numberOfMatchesPlayed = 0

    autoGamePiecesList = []

    # Loop through each match the robot played in.
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
            numGamePieces = 0
            autoScorePos1 = matchResults[analysis.columns.index('autoScore1')]
            autoScorePos2 = matchResults[analysis.columns.index('autoScore2')]
            autoScorePos3 = matchResults[analysis.columns.index('autoScore3')]
            autoScorePos4 = matchResults[analysis.columns.index('autoScore4')]

            if autoScorePos1 > 0:
                numGamePieces += 1
            if autoScorePos2 > 0:
                numGamePieces += 1
            if autoScorePos3 > 0:
                numGamePieces += 1
            if autoScorePos4 > 0:
                numGamePieces += 1

            autoGamePiecesDisplay = numGamePieces
            autoGamePiecesValue = numGamePieces
            autoGamePiecesList.append(autoGamePiecesValue)
            numberOfMatchesPlayed += 1

            # autoScorePos1-4 are 0 if no auto game piece scored, and are 1-27 if a game piece was scored
            if numGamePieces == 0:
                autoGamePiecesColor = 1
            elif numGamePieces == 1:
                autoGamePiecesColor = 2
            elif numGamePieces == 2:
                autoGamePiecesColor =3
            elif numGamePieces == 3:
                autoGamePiecesColor = 4
            elif numGamePieces > 3:
                autoGamePiecesColor = 5
            else:
                print("number of game pieces appear to be negative. Aborting!")
                quit()

            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = str(autoGamePiecesDisplay)
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = autoGamePiecesValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = autoGamePiecesColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(autoGamePiecesList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(autoGamePiecesList), 1))
        rsCEA['S2V'] = round(statistics.median(autoGamePiecesList), 1)
        rsCEA['S2D'] = str(round(statistics.median(autoGamePiecesList), 1))
    return rsCEA