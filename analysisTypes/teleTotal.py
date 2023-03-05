import statistics

def teleTotal(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 8
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    teleTotalList = []
    
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
            
            coneHigh = 0
            coneMid = 0
            coneLow = 0
            cubeHigh = 0
            cubeMid = 0
            cubeLow = 0
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

            teleTotalValue = coneHigh + coneMid + coneLow + cubeHigh + cubeMid + cubeLow
            teleTotalDisplay = (f"{str(teleTotalValue)}")
            teleTotalList.append(teleTotalValue)

            if total == 0:
                teleTotalColor = 1
            elif total <= 3:
                teleTotalColor = 2
            elif total <= 6:
                teleTotalColor = 3
            elif total <= 9:
                teleTotalColor = 4
            else:
                teleTotalColor = 5

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleTotalDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleTotalValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleTotalColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(teleTotalList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(teleTotalList), 1))
        rsCEA['S2V'] = round(statistics.median(teleTotalList), 1)
        rsCEA['S2D'] = str(round(statistics.median(teleTotalList), 1))
    return rsCEA