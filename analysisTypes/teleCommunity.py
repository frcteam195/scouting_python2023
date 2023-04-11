import statistics

def teleCommunity(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 11
    numberOfMatchesPlayed = 0
    teleCommunityList = []
    
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

            display = str(totalCMTY) + "|" + str(LZPickup)
            value = totalCMTY
            if value == 0:
                color = 1
            elif value <= 3:
                color = 2
            elif value <= 6:
                color = 3
            elif value <= 9:
                color = 4
            elif value > 9:
                color = 5
            else:
                print('teleCommunity: that should not happen')
                quit()

            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = display
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = value
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = color

            teleCommunityList.append(value)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(teleCommunityList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(teleCommunityList), 1))
        rsCEA['S2V'] = round(statistics.median(teleCommunityList), 1)
        rsCEA['S2D'] = str(round(statistics.median(teleCommunityList), 1))
        rsCEA['S4V'] = statistics.stdev(teleCommunityList)
    return rsCEA