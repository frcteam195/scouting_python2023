import statistics

def teleWasObstructed(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 14
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    teleWasObstructedList = []
    
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
            
            Obstructed = matchResults[analysis.columns.index('teleWasObstructed')]

            if Obstructed is None:
                Obstructed = 0
            
            if Obstructed == 0:
                teleWasObstructedColor = 1
            elif Obstructed <= 5:
                teleWasObstructedColor = 2
            elif Obstructed <= 10:
                teleWasObstructedColor = 3
            elif Obstructed <= 15:
                teleWasObstructedColor = 4
            elif Obstructed > 15:
                teleWasObstructedColor = 5    
            
            teleWasObstructedDisplay = str(Obstructed)
            teleWasObstructedValue = Obstructed

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleWasObstructedDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleWasObstructedValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleWasObstructedColor

            teleWasObstructedList.append(teleWasObstructedValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(teleWasObstructedList), 1)
    return rsCEA