import statistics

def autoScore(analysis, rsRobotMatchData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 2
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    autoScoreList = []

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
            
            # positionDict = {1: 'autoScore1', 2: 'autoScore2', 3: 'autoScore3', 4: 'autoScore4'}
            # print(positionDict)
            # position = positionDict['1']
            
            scorePos1 = matchResults[analysis.columns.index('autoScore1')]
            scorePos2 = matchResults[analysis.columns.index('autoScore2')]
            scorePos3 = matchResults[analysis.columns.index('autoScore3')]
            scorePos4 = matchResults[analysis.columns.index('autoScore4')]
            
            totalScore = 0

            autoMBdisplay = ""
            autoMB = matchResults[analysis.columns.index('autoMB')]
            if autoMB > 0:
                autoMBdisplay = "*"

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
            
            autoScoreDisplay = str(totalScore) + str(autoMB)
            autoScoreValue = totalScore
            
            if totalScore == 0:
                autoScoreColor = 1
            elif totalScore == 3:
                autoScoreColor = 2
            elif (totalScore >= 4) and (totalScore <= 6):
                autoScoreColor = 3
            elif (totalScore >= 7) and (totalScore <= 12):
                autoScoreColor = 4
            elif (totalScore > 12):
                autoScoreColor = 5

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = autoScoreDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = autoScoreValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = autoScoreColor

            autoScoreList.append(autoScoreValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(autoScoreList), 1)
    return rsCEA