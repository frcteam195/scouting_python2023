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

            teleconeHigh = matchResults[analysis.columns.index('teleConeHigh')]
            teleconeMid = matchResults[analysis.columns.index('teleConeMid')]
            teleconeLow = matchResults[analysis.columns.index('teleConeMid')]

            telecubeHigh = matchResults[analysis.columns.index('teleCubeHigh')]
            telecubeMid = matchResults[analysis.columns.index('teleCubeMid')]
            telecubeLow = matchResults[analysis.columns.index('teleCubeLow')]

            ramp = matchResults[analysis.columns.index('ramp')]

            autoRamp = matchResults[analysis.columns.index('autoRamp')]
            autoRampDisplay = ""

            scorePos1 = matchResults[analysis.columns.index('autoScore1')]
            scorePos2 = matchResults[analysis.columns.index('autoScore2')]
            scorePos3 = matchResults[analysis.columns.index('autoScore3')]
            scorePos4 = matchResults[analysis.columns.index('autoScore4')]
            
            autoScore = 0
            autoMB = matchResults[analysis.columns.index('autoMB')]

            if autoMB is None:
                autoMB = 0

            if (scorePos1 >= 1) and (scorePos1 <= 9):
                autoScore += 6
            elif (scorePos1 >= 10) and (scorePos1 <= 18):
                autoScore += 4
            elif (scorePos1 >= 19) and (scorePos1 <= 27):
                autoScore += 3
            
            if (scorePos2 >= 1) and (scorePos2 <= 9):
                autoScore += 6
            elif (scorePos2 >= 10) and (scorePos2 <= 18):
                autoScore += 4
            elif (scorePos2 >= 19) and (scorePos2 <= 27):
                autoScore += 3

            if (scorePos3 >= 1) and (scorePos3 <= 9):
                autoScore += 6
            elif (scorePos3 >= 10) and (scorePos3 <= 18):
                autoScore += 4
            elif (scorePos3 >= 19) and (scorePos3 <= 27):
                autoScore += 3

            if (scorePos4 >= 1) and (scorePos4 <= 9):
                autoScore += 6
            elif (scorePos4 >= 10) and (scorePos4 <= 18):
                autoScore += 4
            elif (scorePos4 >= 19) and (scorePos4 <= 27):
                autoScore += 3
            
            autoScore += autoMB

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

            if ramp is None:
                ramp = 0
            
            if autoRamp is None:
                autoRamp = 0
                autoRampDisplay = ""
            elif autoRamp > 0:
                autoRampDisplay = "*"
            else:
                autoRampDisplay = ""
                
            teleHigh = teleconeHigh + telecubeHigh
            teleMid = teleconeMid + telecubeMid
            teleLow = teleconeLow + telecubeLow

            total = 0
            
            link = int((teleHigh + teleLow + teleMid) / 3)

            total += autoScore + (teleHigh * 5) + (teleMid * 3) + (teleLow * 2) + link + ramp + autoRamp

            totalScoreDisplay = str(total) + autoRampDisplay
            totalScoreValue = total

            if total <=15:
                totalScoreColor = 1
            elif total <=30:
                totalScoreColor = 2
            elif total <=40:
                totalScoreColor = 3
            elif total <=50:
                totalScoreColor = 4
            elif total > 50:
                totalScoreColor = 5


            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = totalScoreDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = totalScoreValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = totalScoreColor

            totalScoreList.append(totalScoreValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(totalScoreList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(totalScoreList), 1))
        rsCEA['S2V'] = round(statistics.median(totalScoreList), 1)
        rsCEA['S2D'] = str(round(statistics.median(totalScoreList), 1))
    return rsCEA