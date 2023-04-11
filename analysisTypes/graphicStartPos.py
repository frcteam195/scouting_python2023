from ast import Str
import statistics

def graphicStartPos(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 90
    numberOfMatchesPlayed = 0
    startPositionList = []
    rampStatusList = []
    autoRampStatusList = []

    # ramp = 0 = no attempt
    # ramp = 1 = failed attempt
    # ramp = 2 = kept scoring
    # ramp = 3 = parked
    # ramp = 4 = docked
    # ramp = 5 = docked and engaged
    print(len(rsRobotMatchData))
    for matchResults in rsRobotMatchData:
        team = matchResults[analysis.columns.index('team')]
        rsCEA['team'] = str(team)
        rsCEA['eventID'] = matchResults[analysis.columns.index('eventID')]
        preNoShow = matchResults[analysis.columns.index('preNoShow')]
        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if preNoShow != 1 and scoutingStatus == 1:
            startPosition = matchResults[analysis.columns.index('preStartPos')]
            rampStatus = matchResults[analysis.columns.index('ramp')]
            autoRampStatus = matchResults[analysis.columns.index('autoRamp')]

            startPositionList.append(startPosition)
            rampStatusList.append(rampStatus)
            autoRampStatusList.append(autoRampStatus)
            numberOfMatchesPlayed += 1
    
    if numberOfMatchesPlayed > 0:
        # print(f"team = {team}, startPosList = {startPositionList}")
        for position in range(4):  # loop through 4 startin positions
            position += 1
            startPositionPer = (round(startPositionList.count(position)/numberOfMatchesPlayed, 2)) * 100
            if startPositionPer == 0:
                color = '#FFFFFF' # white
            elif startPositionPer < 10:
                color = '#E6F9E6' #1 very light green
            elif startPositionPer < 20:
                color = '#C7F7C7' #2
            elif startPositionPer < 30:
                color = '#A8F5A8' #3
            elif startPositionPer < 40:
                color = '#89F389' #4
            elif startPositionPer < 50:
                color = '#6BEF6B' #5
            elif startPositionPer < 60:
                color = '#4CEC4C' #6
            elif startPositionPer < 70:
                color = '#2DEA2D' #7
            elif startPositionPer < 80:
                color = '#0EE70E' #8
            elif startPositionPer < 90:
                color = '#0CC40C' #9
            elif startPositionPer < 100:
                color = '#0AA10A' #10
            elif startPositionPer == 100:
                color = '#088E08' #11 darker green
            rsCEA['S' + str(position) + 'D'] = str(color)
            rsCEA['S' + str(position) + 'V'] = startPositionPer
            # print(f"percentage {position} = {startPositionPer}")
        
        engaged = rampStatusList.count(5)/numberOfMatchesPlayed
        engaged = round(engaged, 3) * 100
        engagedStr = "{:.0f}".format(engaged)  # added string formatting as the round function was not rounding to 3 digits in all cases
        docked = rampStatusList.count(4)/numberOfMatchesPlayed
        docked = round(docked, 3) * 100
        dockedStr = "{:.0f}".format(docked)
        parked = rampStatusList.count(3)/numberOfMatchesPlayed
        parked = round(parked, 3) * 100
        parkeddStr = "{:.0f}".format(parked)
        # print(f"team = {team}, rampList = {rampStatusList}")
        # print(f"counts = {engagedStr}, {dockedStr}, {parkeddStr}")
        rsCEA['M1D'] = str(engagedStr)
        rsCEA['M1F'] = 0
        rsCEA['M2D'] = str(dockedStr)
        rsCEA['M2F'] = 0
        rsCEA['M3D'] = str(parkeddStr)
        rsCEA['M3F'] = 0
        
        attempts = 0
        for i in autoRampStatusList:
          if i == 1 or i == 2 or i == 3:
              attempts += 1

        if attempts == 0:
            dockedPCT = 0
        else:
            dockedPCT = 100 * (autoRampStatusList.count(2)/attempts)  #docked not engaged
        rsCEA['M4D'] = str(round(dockedPCT, 3))
        
        if attempts == 0:
            engagedPCT = 0
        else:
            engagedPCT = 100 * (autoRampStatusList.count(3)/attempts) #docked and engaged
        rsCEA['M4F'] = str(round(engagedPCT, 3))
        
        # print(autoRampStatusList)
        # print(f"Attempts: {attempts}")
        # print(f"Docked Count: {autoRampStatusList.count(2)}")
        # print(f"Docked Percent: {dockedPCT}")
        # print(f"Engaged Count: {autoRampStatusList.count(3)}")
        # print(f"Engaged: {engagedPCT}")

    return rsCEA
