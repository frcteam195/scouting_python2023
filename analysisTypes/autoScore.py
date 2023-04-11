import statistics

def autoScore(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 2
    numberOfMatchesPlayed = 0
    autoScoreList = []
    
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
            scorePos1 = matchResults[analysis.columns.index('autoScore1')]
            scorePos2 = matchResults[analysis.columns.index('autoScore2')]
            scorePos3 = matchResults[analysis.columns.index('autoScore3')]
            scorePos4 = matchResults[analysis.columns.index('autoScore4')]
            
            totalScore = 0
            autoMB = matchResults[analysis.columns.index('autoMB')]
            if autoMB == 0:
                autoMBdisplay = ""
            elif autoMB == 1:
                autoMBdisplay = ""
            elif autoMB == 2:
                autoMBdisplay = "*"
                totalScore = totalScore + 3
            else:
                autoMBdisplay = '999'

            if (scorePos1 >= 1) and (scorePos1 <= 9):
                totalScore += 6
            elif (scorePos1 >= 10) and (scorePos1 <= 18):
                totalScore += 4
            elif (scorePos1 >= 19) and (scorePos1 <= 27):
                totalScore += 3
            
            if (scorePos2 >= 1) and (scorePos2 <= 9):
                totalScore += 6
            elif (scorePos2 >= 10) and (scorePos2 <= 18):
                totalScore += 4
            elif (scorePos2 >= 19) and (scorePos2 <= 27):
                totalScore += 3

            if (scorePos3 >= 1) and (scorePos3 <= 9):
                totalScore += 6
            elif (scorePos3 >= 10) and (scorePos3 <= 18):
                totalScore += 4
            elif (scorePos3 >= 19) and (scorePos3 <= 27):
                totalScore += 3

            if (scorePos4 >= 1) and (scorePos4 <= 9):
                totalScore += 6
            elif (scorePos4 >= 10) and (scorePos4 <= 18):
                totalScore += 4
            elif (scorePos4 >= 19) and (scorePos4 <= 27):
                totalScore += 3

            autoScoreDisplay = str(totalScore) + str(autoMBdisplay)

            if totalScore == 0:
                autoScoreColor = 1
            elif totalScore <= 3:
                autoScoreColor = 2
            elif totalScore <= 6:
                autoScoreColor = 3
            elif totalScore <= 12:
                autoScoreColor = 4
            else:
                autoScoreColor = 5

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = autoScoreDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = totalScore
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = autoScoreColor

            autoScoreList.append(totalScore)

    if numberOfMatchesPlayed > 0:
        mean = round(statistics.mean(autoScoreList), 1)
        median = round(statistics.median(autoScoreList), 1)
        rsCEA['S1V'] = mean
        rsCEA['S1D'] = str(mean)
        rsCEA['S2V'] = median
        rsCEA['S2D'] = str(median)
        rsCEA['S4V'] = statistics.stdev(autoScoreList)
        
    return rsCEA