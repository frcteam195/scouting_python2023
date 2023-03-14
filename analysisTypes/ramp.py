import statistics
#import mysql.connector
def ramp(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 15
    numberOfMatchesPlayed = 0
    rampList = []
    
    # Loop through each match the robot played in.
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
            ramp = matchResults[analysis.columns.index('ramp')]
            if ramp is None:
                rampValue = 0
            elif ramp == 0:    # no attempt
                rampDisplay = 'NA'
                rampValue = 0
                rampColor = 1
            elif ramp == 1:    # failed attempt, no park
                rampDisplay = 'F'
                rampValue = 0
                rampColor = 1
            elif ramp == 2:    # failed with a park
                rampDisplay = 'F'
                rampValue = 0
                rampColor = 2
            elif ramp == 3:   # parked
                rampDisplay = 2
                rampValue = 2
                rampColor = 3
            elif ramp == 4:   # docked
                rampDisplay = 6
                rampValue = 6
                rampColor = 4
            elif ramp == 5:   # engaged
                rampDisplay = 10
                rampValue = 10
                rampColor = 5
            else:
                rampDisplay = 999
                rampValue = 999
                print(f"ramp = {ramp}")

            rampList.append(rampValue)

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = rampDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = rampValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = rampColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(rampList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(rampList), 1))
        rsCEA['S2V'] = round(statistics.median(rampList), 1)
        rsCEA['S2D'] = str(round(statistics.median(rampList), 1))
    return rsCEA