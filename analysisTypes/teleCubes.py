import statistics

def teleCubes(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 10
    numberOfMatchesPlayed = 0
    teleCubesList = []
    
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
            
            coneHigh = 0
            coneMid = 0
            coneLow = 0

            cubeHigh = 0
            cubeMid = 0
            cubeLow = 0

            totalCubes = 0
            total = 0

            coneHigh = matchResults[analysis.columns.index('teleConeHigh')]
            coneMid = matchResults[analysis.columns.index('teleConeMid')]
            coneLow = matchResults[analysis.columns.index('teleConeLow')]

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

            totalCubes = cubeMid + cubeHigh + cubeLow
            total = coneHigh + coneMid + coneLow + cubeHigh + cubeMid + cubeLow

            teleCubesDisplay = (f"{str(totalCubes)}|{str(total)}")
            teleCubesValue = totalCubes

            if totalCubes == 0:
                teleCubesColor = 1
            elif totalCubes <= 2:
                teleCubesColor = 2
            elif totalCubes <= 4:
                teleCubesColor = 3
            elif totalCubes <= 6:
                teleCubesColor = 4      
            else:
                teleCubesColor = 5

            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleCubesDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleCubesValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleCubesColor

            teleCubesList.append(teleCubesValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(teleCubesList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(teleCubesList), 1))
        rsCEA['S2V'] = round(statistics.median(teleCubesList), 1)
        rsCEA['S2D'] = str(round(statistics.median(teleCubesList), 1))
    
    return rsCEA