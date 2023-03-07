import statistics

def autoScorePosMid(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 82
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
            if (scorePos1 >= 10) and (scorePos1 <= 18):
                autoScoreList.append(scorePos1)
            scorePos2 = matchResults[analysis.columns.index('autoScore2')]
            if (scorePos2 >= 10) and (scorePos2 <= 18):
                autoScoreList.append(scorePos2)
            scorePos3 = matchResults[analysis.columns.index('autoScore3')]
            if (scorePos3 >= 10) and (scorePos3 <= 18):
                autoScoreList.append(scorePos3)
            scorePos4 = matchResults[analysis.columns.index('autoScore4')]
            if (scorePos4 >= 10) and (scorePos4 <= 18):
                autoScoreList.append(scorePos4)

            numberOfMatchesPlayed += 1
            
    if numberOfMatchesPlayed > 0:
        position = 0
        for count in range(9):
            count += 1
            position += 10
            value = round(autoScoreList.count(position)/numberOfMatchesPlayed, 1)
            rsCEA['M' + str(count) + 'D'] = value
        
    return rsCEA