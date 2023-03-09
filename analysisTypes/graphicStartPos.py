from ast import Str
import statistics

def graphicStartPos(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 90
    numberOfMatchesPlayed = 0
    graphicStartPos = []

    startPosTotal1 = 0
    startPosTotal2 = 0
    startPosTotal3 = 0
    startPosTotal4 = 0

    startPosColor1 = 0
    startPosColor2 = 0
    startPosColor3 = 0
    startPosColor4 = 0

    rampTotal1 = 0 #docked engaged
    rampTotal2 = 0 #docked
    rampTotal3 = 0 #park
    rampTotal4 = 0 #no attempt
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
            preStartPos = matchResults[analysis.columns.index('preStartPos')]
            ramp = matchResults[analysis.columns.index('ramp')]

            if preStartPos is None:
                preStartPos = 0
            if ramp is None:
                ramp = 0

            if preStartPos == 1:
                startPosTotal1 +=1
            if preStartPos == 2:
                startPosTotal2 +=1
            if preStartPos == 3:
                startPosTotal3 +=1
            if preStartPos == 4:
                startPosTotal4 +=1

            if ramp == 5:
                rampTotal1 += 1
            elif ramp == 4:
                rampTotal2 += 1
            elif ramp == 3:
                rampTotal3 += 1
            elif ramp == 0:
                rampTotal4 += 1

            numberOfMatchesPlayed += 1
            
            graphicStartPos.append(0)
    
    if numberOfMatchesPlayed > 0:
        startPosTotal = startPosTotal1 +  startPosTotal2 +  startPosTotal3 +  startPosTotal4
        if startPosTotal1 == 0:
            percent1 = 0
        else:
            percent1 = int(startPosTotal1 / startPosTotal * 100)
        if startPosTotal2 == 0:
            percent2 = 0
        else:
            percent2 = int(startPosTotal2 / startPosTotal * 100)
        if startPosTotal3 == 0:
            percent3 = 0
        else:
            percent3 = int(startPosTotal3 / startPosTotal * 100)
        if startPosTotal4 == 0:
            percent4 = 0
        else:
            percent4 = int(startPosTotal4 / startPosTotal * 100)

        rampTotal = rampTotal1 + rampTotal2 + rampTotal3 + rampTotal4

        if rampTotal1 == 0:
            rampPercent1 = 0
        else:
            rampPercent1 = int(rampTotal1 / rampTotal * 100)
            
        if rampTotal2 == 0:
            rampPercent2 = 0
        else:
            rampPercent2 = int(rampTotal2 / rampTotal * 100)
            
        if rampTotal3 == 0:
            rampPercent3 = 0
        else:
            rampPercent3 = int(rampTotal3 / rampTotal * 100)
            
        if rampTotal4 == 0:
            rampPercent4 = 0
        else:
            rampPercent4 = int(rampTotal4 / rampTotal * 100)

    startPosTotals = [startPosTotal1, startPosTotal2, startPosTotal3, startPosTotal4]
    sortedList = sorted(startPosTotals, reverse=False)

    # print(sortedList)
    # startPosTotals = sorted(startPosTotals, reverse= True)

    # assign the colors to the corresponding variables

    # print(sortedList.index(startPosTotal1)+1)
    # print(sortedList.index(startPosTotal2)+1)
    # print(sortedList.index(startPosTotal3)+1)
    # print(sortedList.index(startPosTotal4)+1)

    rsCEA['S1D'] = percent1
    rsCEA['S1F'] = startPosColor1
    rsCEA['S1V'] = rampPercent1

    rsCEA['S2D'] = percent2
    rsCEA['S2F'] = startPosColor2
    rsCEA['S2V'] = rampPercent2

    rsCEA['S3D'] = percent3
    rsCEA['S3F'] = startPosColor3
    rsCEA['S3V'] = rampPercent3

    rsCEA['S4D'] = percent4
    rsCEA['S4F'] = startPosColor4
    rsCEA['S4V'] = rampPercent4



    return rsCEA