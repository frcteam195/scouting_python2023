import statistics

def teleObstructed(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 13
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    teleObstructedList = []
    
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
            
            Obstructed = matchResults[analysis.columns.index('teleObstructed')]

            if Obstructed is None:
                Obstructed = 0
            
            if Obstructed == 0:
                teleObstructedColor = 1
            elif Obstructed <= 5:
                teleObstructedColor = 2
            elif Obstructed <= 10:
                teleObstructedColor = 3
            elif Obstructed <= 15:
                teleObstructedColor = 4
            elif Obstructed > 15:
                teleObstructedColor = 5    
            
            teleObstructedDisplay = str(Obstructed)
            teleObstructedValue = Obstructed

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleObstructedDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleObstructedValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleObstructedColor

            teleObstructedList.append(teleObstructedValue)

    if numberOfMatchesPlayed > 0:
        mean = round(statistics.mean(teleObstructedList), 1)
        median = round(statistics.median(teleObstructedList), 1)
        rsCEA['S1V'] = mean
        rsCEA['S1D'] = str(mean)
        if mean == 0:
            rsCEA['S1F'] = 1
        elif mean <= 5:
            rsCEA['S1F'] = 2
        elif mean <= 10:
            rsCEA['S1F'] = 3
        elif mean <= 15:
            rsCEA['S1F'] = 4
        elif mean > 15:
            rsCEA['S1F'] = 5
        else:
            rsCEA['S1F'] = 999
        rsCEA['S2V'] = median
        rsCEA['S2D'] = str(median)
        if median == 0:
            rsCEA['S1F'] = 1
        elif median <= 5:
            rsCEA['S1F'] = 2
        elif median <= 10:
            rsCEA['S1F'] = 3
        elif median <= 15:
            rsCEA['S1F'] = 4
        elif median > 15:
            rsCEA['S1F'] = 5
        else:
            rsCEA['S1F'] = 999
    return rsCEA