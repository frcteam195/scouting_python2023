from ast import Str
import statistics

def autoGamePieces(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 3
    numberOfMatchesPlayed = 0

    autoGamePiecesList = []

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
            autoScorePos1 = matchResults[analysis.columns.index('autoScore1')]
            autoScorePos2 = matchResults[analysis.columns.index('autoScore2')]
            autoScorePos3 = matchResults[analysis.columns.index('autoScore3')]
            autoScorePos4 = matchResults[analysis.columns.index('autoScore4')]

            numGamePieces = 0
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
                autoGamePiecesColor = 3
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
        mean = round(statistics.mean(autoGamePiecesList), 1)
        median = round(statistics.median(autoGamePiecesList), 1)
        rsCEA['S1V'] = mean
        rsCEA['S1D'] = str(mean)
        rsCEA['S2V'] = median
        rsCEA['S2D'] = str(median)
    return rsCEA