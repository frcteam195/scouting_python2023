import statistics
#import mysql.connector
def ramp(analysis, rsRobotMatchData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 15
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    rampList = []
    
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
            
            ramp = matchResults[analysis.columns.index('ramp')]
            if ramp is None:
                ramp = 0

            rampDisplay = ramp
            rampValue = ramp
            
            if ramp == 2:
                rampColor = 3
            elif ramp == 3:
                rampColor = 2
            else:
                rampColor = ramp #it happened to be that the color id is pretty similar to the ramp value
            

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = rampDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = rampValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = rampColor

            rampList.append(rampValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(rampList), 1)
    return rsCEA