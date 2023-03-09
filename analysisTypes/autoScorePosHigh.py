from multiprocessing.sharedctypes import Value

def autoScorePosHigh(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 81
    numberOfMatchesPlayed = 0

    autoScorePosHighList = []
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
            value = (round(autoScoreList.count(position)/numberOfMatchesPlayed, 2)) * 100
            if value == 0:
                color = '#70FF00'
            elif value < 10:
                color = '#A0FF00' 
            elif value < 20:
                color = '#D0FF00' 
            elif value < 30:
                color = '#FFFF00' 
            elif value < 40:
                color = '#FFE000'  
            elif value < 50:
                color = '#FFC000' 
            elif value < 60:
                color = '#FFA000' 
            elif value < 70:
                color = '#FF8000' 
            elif value < 80:
                color = '#FF6000' 
            elif value < 90:
                color = '#FF4000'
            elif value < 100:
                color = '#FF2000'
            elif value == 100:
                color = '#FF0000'
            else:
                print('autoScorePosHigh: That should not happen')
                quit()
            position += 1

            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = str(color)
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = value

            autoScorePosHighList.append(value)

    return rsCEA