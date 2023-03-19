import statistics
def teleScore(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 27
    numberOfMatchesPlayed = 0

    teleScoreList = []
    
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

            if ramp is None:
                ramp = 0

            total = 0
            teleHigh = teleconeHigh + telecubeHigh
            teleMid = teleconeMid + telecubeMid
            teleLow = teleconeLow + telecubeLow
            link = int((teleHigh + teleLow + teleMid) / 3)

            total += (teleHigh * 5) + (teleMid * 3) + (teleLow * 2) + link + ramp

            teleScoreDisplay = total
            teleScoreValue = total

            if total <= 12:
                teleScoreColor = 1
            elif total <=24:
                teleScoreColor = 2
            elif total <= 36:
                teleScoreColor = 3
            elif total <=48:
                teleScoreColor = 4
            elif total > 48:
                teleScoreColor = 5
            


            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleScoreDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleScoreValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleScoreColor

            teleScoreList.append(teleScoreValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(teleScoreList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(teleScoreList), 1))
        rsCEA['S2V'] = round(statistics.median(teleScoreList), 1)
        rsCEA['S2D'] = str(round(statistics.median(teleScoreList), 1))
    return rsCEA