from ast import Str
import statistics

def graphicTeleInfo(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 91
    numberOfMatchesPlayed = 0
    graphicTeleInfoList = []
    teleTotal = []

    totalHigh = 0
    totalMid = 0
    totalLow = 0
    total = 0
    totalCones = 0
    totalCubes = 0
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
            teleConeHigh = matchResults[analysis.columns.index('teleConeHigh')]
            teleConeMid = matchResults[analysis.columns.index('teleConeMid')]
            teleConeLow = matchResults[analysis.columns.index('teleConeLow')]

            teleCubeHigh = matchResults[analysis.columns.index('teleCubeHigh')]
            teleCubeMid = matchResults[analysis.columns.index('teleCubeMid')]
            teleCubeLow = matchResults[analysis.columns.index('teleCubeLow')]
            teleTotal = matchResults[analysis.columns.index('teleTotal')]
            if(teleConeHigh is None):
                teleConeHigh = 0
            if(teleConeMid is None):
                teleConeMid = 0
            if(teleConeLow is None):
                teleConeLow = 0
            if(teleCubeHigh is None):
                teleCubeHigh = 0
            if(teleCubeMid is None):
                teleCubeMid = 0
            if(teleCubeLow is None):
                teleCubeLow = 0
            if(teleTotal is None):
                teleTotal = 0

            totalHigh += (teleConeHigh + teleCubeHigh)
            totalMid += (teleConeMid + teleCubeMid)
            totalLow += (teleConeLow + teleCubeLow)

            totalCones += (teleConeHigh + teleConeLow + teleConeMid)
            totalCubes += (teleCubeHigh + teleCubeMid + teleCubeLow)

            teleTotal += (totalCones + totalCubes)
            numberOfMatchesPlayed += 1
            
            graphicTeleInfoList.append(0)
            
    total = (totalHigh + totalLow + totalMid)
    if(totalHigh == 0):
        percentHigh = 0
    else:
        percentHigh = int(totalHigh / total * 100)
    
    if(totalMid == 0):
        percentMid = 0
    else:
        percentMid = int(totalMid / total * 100)
    
    if(totalLow == 0):
        percentLow = 0
    else:
        percentLow = int(totalLow / total * 100)
    
    if(totalCones == 0):
        percentCones = 0
    else:
        percentCones = int(totalCones / (totalCones + totalCubes) * 100)
    
    if(totalCubes == 0):
        percentCubes = 0
    else:
        percentCubes = int(totalCubes / (totalCones + totalCubes) * 100)

    highDisplay = 0
    midDisplay = 0
    lowDisplay = 0

    if totalHigh > totalMid and totalHigh > totalLow:
        highDisplay = 4
        midDisplay = 3 if totalMid > totalLow else \
                    2 if totalMid < totalLow else \
                    3 if totalMid == totalLow else midDisplay
        lowDisplay = 3 if totalLow > totalMid else \
                    2 if totalLow < totalMid else \
                    3 if totalLow == totalMid else lowDisplay
    elif totalMid > totalHigh and totalMid > totalLow:
        midDisplay = 4
        highDisplay = 3 if totalHigh > totalLow else \
                    2 if totalHigh < totalLow else \
                    3 if totalHigh == totalLow else highDisplay
        lowDisplay = 3 if totalLow > totalHigh else \
                    2 if totalLow < totalHigh else \
                    3 if totalLow == totalHigh else lowDisplay
    elif totalLow > totalMid and totalLow > totalHigh:
        lowDisplay = 4
        highDisplay = 3 if totalHigh > totalMid else \
                    2 if totalHigh < totalMid else \
                    3 if totalHigh == totalMid else highDisplay
        midDisplay = 3 if totalMid > totalHigh else \
                    2 if totalMid < totalHigh else \
                    3 if totalMid == totalHigh else midDisplay
    elif totalLow == totalMid and totalLow > totalHigh:
        lowDisplay = 4
        midDisplay = 4
        highDisplay = 2
    elif totalLow == totalHigh and totalLow > totalMid:
        lowDisplay = 4
        highDisplay = 4
        midDisplay = 2
    elif totalHigh == totalMid and totalHigh > totalLow:
        highDisplay = 4
        midDisplay = 4
        lowDisplay = 2


    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = totalHigh
        rsCEA['S1D'] = percentHigh
        rsCEA['S1F'] = highDisplay
        
        rsCEA['S2V'] = totalMid
        rsCEA['S2D'] = percentMid
        rsCEA['S2F'] = midDisplay
        
        rsCEA['S3V'] = totalLow
        rsCEA['S3D'] = percentLow
        rsCEA['S3F'] = lowDisplay
        
        rsCEA['S4D'] = percentCones
        rsCEA['S4V'] = percentCubes

        rsCEA['M12D'] = totalCones
        rsCEA['M12V'] = totalCubes

        rsCEA['M11V'] = totalHigh
        rsCEA['M11D'] = totalMid
        rsCEA['M11F'] = totalLow
        rsCEA['S5D'] = str(round(statistics.mean(graphicTeleInfoList), 1))
    return rsCEA