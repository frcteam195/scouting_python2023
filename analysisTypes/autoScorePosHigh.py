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
            value = (round(autoScoreList.count(position)/numberOfMatchesPlayed, 1)) * 100
            rsCEA['M' + str(count) + 'F'] = value
            if value == 0:
                rsCEA['M' + str(count) + 'D'] = '#70FF00'
            elif value < 10:
                rsCEA['M' + str(count) + 'D'] = '#A0FF00' 
            elif value < 20:
                rsCEA['M' + str(count) + 'D'] = '#D0FF00' 
            elif value < 30:
                rsCEA['M' + str(count) + 'D'] = '#FFFF00' 
            elif value < 40:
                rsCEA['M' + str(count) + 'D'] = '#FFE000'  
            elif value < 50:
                rsCEA['M' + str(count) + 'D'] = '#FFC000' 
            elif value < 60:
                rsCEA['M' + str(count) + 'D'] = '#FFA000' 
            elif value < 70:
                rsCEA['M' + str(count) + 'D'] = '#FF8000' 
            elif value < 80:
                rsCEA['M' + str(count) + 'D'] = '#FF6000' 
            elif value < 90:
                rsCEA['M' + str(count) + 'D'] = '#FF4000'
            elif value < 100:
                rsCEA['M' + str(count) + 'D'] = '#FF2000'
            elif value == 100:
                rsCEA['M' + str(count) + 'D'] = '#FF0000'
            else:
                print('autoScorePosHigh: That should not happen')
                quit()
            position += 1
    return rsCEA