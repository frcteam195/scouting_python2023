import statistics

# Note: This was changed to reflect slider pkup for CT Champs, but leaving the post in the name for simplicity
#       also changed to a simple numberic value. DB changed to insert a zero by defaut

def teleLZPickup(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 12
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    teleLZPickupList = []
    
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
            LZPickup = matchResults[analysis.columns.index('teleLZPickup')]
     
            if LZPickup is None:
                LZPickup = 0
                
            teleLZPickupDisplay = str(LZPickup)
            teleLZPickupValue = LZPickup

            if LZPickup == 0:
                teleLZPickupColor = 1
            elif LZPickup <= 2:
                teleLZPickupColor = 2
            elif LZPickup <= 4:
                teleLZPickupColor = 3
            elif LZPickup <= 6:
                teleLZPickupColor = 4
            else:
                teleLZPickupColor = 5

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleLZPickupDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleLZPickupValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleLZPickupColor

            teleLZPickupList.append(teleLZPickupValue)

    if numberOfMatchesPlayed > 0:
        mean = round(statistics.mean(teleLZPickupList), 1)
        median = round(statistics.median(teleLZPickupList), 1)
        if len(teleLZPickupList) >= 2:
            stdev = statistics.stdev(teleLZPickupList)
        else:
            stdev = 0

        rsCEA['S1V'] = mean
        rsCEA['S1D'] = str(mean)
        rsCEA['S2V'] = median
        rsCEA['S2D'] = str(median)
        rsCEA['S4V'] = stdev
    return rsCEA