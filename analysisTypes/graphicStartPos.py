from ast import Str
import statistics

def graphicStartPos(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 90
    numberOfMatchesPlayed = 0
    startPositionList = []
    rampStatusList = []

    # ramp = 0 = no attempt
    # ramp = 1 = failed attempt
    # ramp = 2 = kept scoring
    # ramp = 3 = parked
    # ramp = 4 = docked
    # ramp = 5 = docked and engaged

    for matchResults in rsRobotMatchData:
        team = matchResults[analysis.columns.index('team')]
        rsCEA['team'] = str(team)
        rsCEA['eventID'] = matchResults[analysis.columns.index('eventID')]
        preNoShow = matchResults[analysis.columns.index('preNoShow')]
        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if preNoShow != 1 and scoutingStatus == 1:
            startPosition = matchResults[analysis.columns.index('preStartPos')]
            rampStatus = matchResults[analysis.columns.index('ramp')]

            startPositionList.append(startPosition)
            rampStatusList.append(rampStatus)
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
        
        
        engaged = (round(rampStatusList.count(5)/numberOfMatchesPlayed),3) * 100
        docked = (round(rampStatusList.count(4)/numberOfMatchesPlayed), 3) * 100
        parked = (round(rampStatusList.count(3)/numberOfMatchesPlayed), 3) * 100
        # print(f"team = {team}, rampList = {rampStatusList}")
        # print(f"counts = {engaged}, {docked}, {parked}")
        rsCEA['M1D'] = str(engaged)
        rsCEA['M1F'] = 0
        rsCEA['M2D'] = str(docked)
        rsCEA['M2F'] = 0
        rsCEA['M3D'] = str(parked)
        rsCEA['M3F'] = 0
        
    return rsCEA
