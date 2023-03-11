import statistics

def autoScorePosLow(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 83
    numberOfMatchesPlayed = 0
    autoScoreList = []
    
    for matchResults in rsRobotMatchData:
        rsCEA['team'] = matchResults[analysis.columns.index('team')]
        team = matchResults[analysis.columns.index('team')]
        teamMatchNum = matchResults[analysis.columns.index('teamMatchNum')]
        rsCEA['eventID'] = matchResults[analysis.columns.index('eventID')]
        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if scoutingStatus == 1:  
            scorePos1 = matchResults[analysis.columns.index('autoScore1')]
            if (scorePos1 >= 19) and (scorePos1 <= 27):
                autoScoreList.append(scorePos1)
            scorePos2 = matchResults[analysis.columns.index('autoScore2')]
            if (scorePos2 >= 19) and (scorePos2 <= 27):
                autoScoreList.append(scorePos2)
            scorePos3 = matchResults[analysis.columns.index('autoScore3')]
            if (scorePos3 >= 19) and (scorePos3 <= 27):
                autoScoreList.append(scorePos3)
            scorePos4 = matchResults[analysis.columns.index('autoScore4')]
            if (scorePos4 >= 19) and (scorePos4 <= 27):
                autoScoreList.append(scorePos4)
            # print(f"team = {team}, teamMatchNum = {teamMatchNum}, list = {autoScoreList}")

            numberOfMatchesPlayed += 1
            
    if numberOfMatchesPlayed > 0:
        position = 19
        for count in range(9):
            count += 1
            value = None
            # print(f"Low - Team = {teamNum}, count = {count}, position = {position}, list = {autoScoreList}")
            value = (round(autoScoreList.count(position)/numberOfMatchesPlayed, 2)) * 100
            # print(f"count = {count}, position = {position}, Low value = {value}")
            if value == None:
                value = 0
            if value == 0:
                color = '#FFFFFF' # white
            elif value < 10:
                color = '#E6F9E6' #1 very light green
            elif value < 20:
                color = '#C7F7C7' #2
            elif value < 30:
                color = '#A8F5A8' #3
            elif value < 40:
                color = '#89F389' #4
            elif value < 50:
                color = '#6BEF6B' #5
            elif value < 60:
                color = '#4CEC4C' #6
            elif value < 70:
                color = '#2DEA2D' #7
            elif value < 80:
                color = '#0EE70E' #8
            elif value < 90:
                color = '#0CC40C' #9
            elif value < 100:
                color = '#0AA10A' #10
            elif value == 100:
                color = '#088E08' #11 darker green
            else:
                print('autoScorePosLow: That should not happen')
                quit()
            position += 1

            rsCEA['M' + str(count) + 'D'] = str(color)
            rsCEA['M' + str(count) + 'V'] = value

    return rsCEA