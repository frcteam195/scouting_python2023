import statistics
def totalScore(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 26
    numberOfMatchesPlayed = 0

    totalScoreList = []
    
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
            autoMB = matchResults[analysis.columns.index('autoMB')]
            scorePos1 = matchResults[analysis.columns.index('autoScore1')]
            scorePos2 = matchResults[analysis.columns.index('autoScore2')]
            scorePos3 = matchResults[analysis.columns.index('autoScore3')]
            scorePos4 = matchResults[analysis.columns.index('autoScore4')]
            autoRamp = matchResults[analysis.columns.index('autoRamp')]
            
            teleconeHigh = matchResults[analysis.columns.index('teleConeHigh')]
            teleconeMid = matchResults[analysis.columns.index('teleConeMid')]
            teleconeLow = matchResults[analysis.columns.index('teleConeLow')]
            telecubeHigh = matchResults[analysis.columns.index('teleCubeHigh')]
            telecubeMid = matchResults[analysis.columns.index('teleCubeMid')]
            telecubeLow = matchResults[analysis.columns.index('teleCubeLow')]

            ramp = matchResults[analysis.columns.index('ramp')]

            # auto
            if autoMB == 2:
                moveBonusPts = 3
            else:
                moveBonusPts = 0
            
            autoGPscore = 0
            if (scorePos1 >= 1) and (scorePos1 <= 9):
                autoGPscore += 6
            elif (scorePos1 >= 10) and (scorePos1 <= 18):
                autoGPscore += 4
            elif (scorePos1 >= 19) and (scorePos1 <= 27):
                autoGPscore += 3
            
            if (scorePos2 >= 1) and (scorePos2 <= 9):
                autoGPscore += 6
            elif (scorePos2 >= 10) and (scorePos2 <= 18):
                autoGPscore += 4
            elif (scorePos2 >= 19) and (scorePos2 <= 27):
                autoGPscore += 3

            if (scorePos3 >= 1) and (scorePos3 <= 9):
                autoGPscore += 6
            elif (scorePos3 >= 10) and (scorePos3 <= 18):
                autoGPscore += 4
            elif (scorePos3 >= 19) and (scorePos3 <= 27):
                autoGPscore += 3

            if (scorePos4 >= 1) and (scorePos4 <= 9):
                autoGPscore += 6
            elif (scorePos4 >= 10) and (scorePos4 <= 18):
                autoGPscore += 4
            elif (scorePos4 >= 19) and (scorePos4 <= 27):
                autoGPscore += 3
            
            if autoRamp is None:
                autoRampDisplay = ""
                autoRampPts = 0
            elif autoRamp == 5:
                autoRampDisplay = "*"
                autoRampPts = 12
            elif autoRamp == 4:
                autoRampDisplay = "*"
                autoRampPts = 8
            else:
                autoRampPts = 0
                autoRampDisplay = ""

            autoScore = autoGPscore + moveBonusPts + autoRampPts

            # teleop
            if teleconeHigh is None:
                teleconeHigh = 0
            if teleconeMid is None:
                teleconeMid = 0
            if teleconeLow is None:
                teleconeLow = 0
            if telecubeHigh is None:
                telecubeHigh = 0
            if telecubeMid is None:
                telecubeMid = 0
            if telecubeLow is None:
                telecubeLow = 0

            teleHigh = teleconeHigh + telecubeHigh
            teleMid = teleconeMid + telecubeMid
            teleLow = teleconeLow + telecubeLow

            linkPts = (teleHigh + teleMid + teleLow) / 3

            telePts = (teleHigh * 5) + (teleMid * 3) + (teleLow * 2) + linkPts

            # end-game
            if ramp == 5:
                rampPts = 10
            elif ramp == 4:
                rampPts = 6
            elif ramp == 3:
                rampPts = 2
            elif ramp == 2:
                rampPts = 2
            else:
                rampPts = 0
            
            totalScore = 0
            totalScore = autoScore + telePts + rampPts + autoRamp

            totalScoreDisplay = str(totalScore) + autoRampDisplay
            totalScoreValue = totalScore

            if totalScore <=15:
                totalScoreColor = 1
            elif totalScore <=30:
                totalScoreColor = 2
            elif totalScore <=40:
                totalScoreColor = 3
            elif totalScore <=50:
                totalScoreColor = 4
            elif totalScore > 50:
                totalScoreColor = 5

            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = str(int(totalScoreDisplay))
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = totalScoreValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = totalScoreColor

            totalScoreList.append(totalScoreValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(totalScoreList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(totalScoreList), 1))
        rsCEA['S2V'] = round(statistics.median(totalScoreList), 1)
        rsCEA['S2D'] = str(round(statistics.median(totalScoreList), 1))
    return rsCEA