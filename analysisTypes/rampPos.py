import statistics
#import mysql.connector
def rampPos(analysis, rsRobotMatchData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 16
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    rampPosList = []
    
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
            
            rampPos = matchResults[analysis.columns.index('rampPos')]
            ramp = matchResults[analysis.columns.index('ramp')]
            
            if rampPos is None:
                rampPos = 0
            if ramp is None:
                ramp = 0

            rampPosDisplay = rampPos
            rampPosValue = rampPos
            
            if rampPos == 0:
                rampPosColor = 3
            elif rampPos == 1:
                rampPosColor = 4
            elif rampPos == 2:
                rampPosColor = 4
            
            if ramp == 1:
                rampPosColor = 2
            

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = rampPosDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = rampPosValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = rampPosColor

            rampPosList.append(rampPosValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(rampPosList), 1)
    return rsCEA