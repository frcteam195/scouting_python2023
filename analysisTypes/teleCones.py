import statistics

def teleCones(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 9
    numberOfMatchesPlayed = 0

    teleConesList = []
    
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
            
            coneHigh = 0
            coneMid = 0
            coneLow = 0

            cubeHigh = 0
            cubeMid = 0
            cubeLow = 0

            totalCones = 0
            total = 0

            coneHigh = matchResults[analysis.columns.index('teleConeHigh')]
            coneMid = matchResults[analysis.columns.index('teleConeMid')]
            coneLow = matchResults[analysis.columns.index('teleConeMid')]

            cubeHigh = matchResults[analysis.columns.index('teleCubeHigh')]
            cubeMid = matchResults[analysis.columns.index('teleCubeMid')]
            cubeLow = matchResults[analysis.columns.index('teleCubeLow')]


            if coneHigh is None:
                coneHigh = 0
            if coneMid is None:
                coneMid = 0
            if coneLow is None:
                coneLow = 0
            if cubeHigh is None:
                cubeHigh = 0
            if cubeMid is None:
                cubeMid = 0
            if cubeLow is None:
                cubeLow = 0

            totalCones = coneMid + coneHigh + coneLow
            total = coneHigh + coneMid + coneLow + cubeHigh + cubeMid + cubeLow

            teleConesDisplay = (f"{str(totalCones)}|{str(total)}")
            teleConesValue = totalCones

            if total == 0:
                teleConesColor = 1
            elif total <= 3:
                teleConesColor = 2
            elif total <= 6:
                teleConesColor = 3
            elif total <= 9:
                teleConesColor = 4
            else:
                teleConesColor = 5


            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleConesDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleConesValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleConesColor

            teleConesList.append(teleConesValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(teleConesList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(teleConesList), 1))
        rsCEA['S2V'] = round(statistics.median(teleConesList), 1)
        rsCEA['S2D'] = str(round(statistics.median(teleConesList), 1))
    return rsCEA