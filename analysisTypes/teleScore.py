import statistics
def teleScore(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 27
    numberOfMatchesPlayed = 0
    teleScoreList = []
    
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
            teleconeHigh = matchResults[analysis.columns.index('teleConeHigh')]
            teleconeMid = matchResults[analysis.columns.index('teleConeMid')]
            teleconeLow = matchResults[analysis.columns.index('teleConeLow')]
            telecubeHigh = matchResults[analysis.columns.index('teleCubeHigh')]
            telecubeMid = matchResults[analysis.columns.index('teleCubeMid')]
            telecubeLow = matchResults[analysis.columns.index('teleCubeLow')]
            ramp = matchResults[analysis.columns.index('ramp')]
            
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
            teleTotal = teleLow + teleMid + teleHigh
            linkPts = (teleTotal / 3) * 5

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
            
            teleScore = 0
            teleScore = (teleHigh * 5) + (teleMid * 3) + (teleLow * 2) + linkPts + rampPts
            teleScore = round(teleScore)

            if teleScore <= 12:
                teleScoreColor = 1
            elif teleScore <= 24:
                teleScoreColor = 2
            elif teleScore <= 36:
                teleScoreColor = 3
            elif teleScore <= 48:
                teleScoreColor = 4
            elif teleScore > 48:
                teleScoreColor = 5

            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = str(teleScore)
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleScore
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleScoreColor

            teleScoreList.append(teleScore)
            numberOfMatchesPlayed += 1

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(teleScoreList), 0)
        rsCEA['S1D'] = str(round(statistics.mean(teleScoreList), 0))
        rsCEA['S2V'] = round(statistics.median(teleScoreList), 0)
        rsCEA['S2D'] = str(round(statistics.median(teleScoreList), 0))
        rsCEA['S4V'] = statistics.stdev(teleScoreList)
        
    return rsCEA