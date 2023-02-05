import statistics

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
            elif LZPickup <= 3:
                teleLZPickupColor = 2
            elif LZPickup <= 6:
                teleLZPickupColor = 3
            elif LZPickup <= 9:
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
        rsCEA['S1V'] = round(statistics.mean(teleLZPickupList), 1)
    return rsCEA