import statistics

def teleCommunity(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 11
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    teleCommunityList = []
    
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
            
            
            coneCMTY = matchResults[analysis.columns.index('teleConeCMTY')]
            cubeCMTY = matchResults[analysis.columns.index('teleCubeCMTY')]
            LZPickup = matchResults[analysis.columns.index('teleLZPickup')]

            if coneCMTY is None:
                coneCMTY = 0
            if cubeCMTY is None:
                cubeCMTY = 0
            if LZPickup is None:
                LZPickup = 0


            totalCMTY = coneCMTY + cubeCMTY

            teleCommunityDisplay = str(totalCMTY) + "|" + str(LZPickup)
            teleCommunityValue = totalCMTY
            if LZPickup is None:
                teleCommunityColor = 1
            elif LZPickup == 0:
                teleCommunityColor = 1
            elif LZPickup <= 3:
                teleCommunityColor = 2
            elif LZPickup <= 6:
                teleCommunityColor = 3
            elif LZPickup <= 9:
                teleCommunityColor = 4
            else:
                teleCommunityColor = 5

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleCommunityDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleCommunityValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleCommunityColor

            teleCommunityList.append(teleCommunityValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(teleCommunityList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(teleCommunityList), 1))
        rsCEA['S2V'] = round(statistics.median(teleCommunityList), 1)
        rsCEA['S2D'] = str(round(statistics.median(teleCommunityList), 1))
    return rsCEA