import statistics

def autoScorePosHigh(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 81
    numberOfMatchesPlayed = 0
    autoScoreList = []
    
    for matchResults in rsRobotMatchData:
        rsCEA['team'] = matchResults[analysis.columns.index('team')]
        teamNum = matchResults[analysis.columns.index('team')]
        rsCEA['eventID'] = matchResults[analysis.columns.index('eventID')]
        preNoShow = matchResults[analysis.columns.index('preNoShow')]
        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if preNoShow == 1:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'DNS'
        elif scoutingStatus == 2:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'UR'
        else:  
            scorePos1 = matchResults[analysis.columns.index('autoScore1')]
            if (scorePos1 >= 1) and (scorePos1 <= 9):
                autoScoreList.append(scorePos1)
            scorePos2 = matchResults[analysis.columns.index('autoScore2')]
            if (scorePos2 >= 1) and (scorePos2 <= 9):
                autoScoreList.append(scorePos2)
            scorePos3 = matchResults[analysis.columns.index('autoScore3')]
            if (scorePos3 >= 1) and (scorePos3 <= 9):
                autoScoreList.append(scorePos3)
            scorePos4 = matchResults[analysis.columns.index('autoScore4')]
            if (scorePos4 >= 1) and (scorePos4 <= 9):
                autoScoreList.append(scorePos4)

            numberOfMatchesPlayed += 1
            
    if numberOfMatchesPlayed > 0:
        position = 1
        for count in range(9):
            count += 1
            # print(f"High - Team = {teamNum}, count = {count}, position = {position}, list = {autoScoreList}")
            value = round(autoScoreList.count(position)/numberOfMatchesPlayed, 1)
            rsCEA['M' + str(count) + 'D'] = value
            if value == 0:
                rsCEA['M' + str(count) + 'F'] = 100
            elif value < 0.1:
                rsCEA['M' + str(count) + 'F'] = 101
            elif value < 0.2:
                rsCEA['M' + str(count) + 'F'] = 102
            elif value < 0.3:
                rsCEA['M' + str(count) + 'F'] = 103
            elif value < 0.4:
                rsCEA['M' + str(count) + 'F'] = 104
            elif value < 0.5:
                rsCEA['M' + str(count) + 'F'] = 105
            elif value < 0.6:
                rsCEA['M' + str(count) + 'F'] = 106
            elif value < 0.7:
                rsCEA['M' + str(count) + 'F'] = 107
            elif value < 0.8:
                rsCEA['M' + str(count) + 'F'] = 108
            elif value < 0.9:
                rsCEA['M' + str(count) + 'F'] = 109
            elif value < 1.0:
                rsCEA['M' + str(count) + 'F'] = 110
            elif value == 1:
                rsCEA['M' + str(count) + 'F'] = 111
            else:
                print('autoScorePosHigh: That should not happen')
                quit()
            position += 1
    return rsCEA