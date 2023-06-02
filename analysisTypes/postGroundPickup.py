import statistics
#import mysql.connector
def postGroundPickup(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 21
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    teleGroundPickupList = []
    
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
            teleGroundPickup = matchResults[analysis.columns.index('teleGroundPickup')]
            
            teleGroundPickupDisplay = str(teleGroundPickup)
            teleGroundPickupValue = teleGroundPickup

            if teleGroundPickup == 0:
                teleGroundPickupColor = 1
            elif teleGroundPickup <= 2:
                teleGroundPickupColor = 2
            elif teleGroundPickup <= 4:
                teleGroundPickupColor = 3
            elif teleGroundPickup <= 6:
                teleGroundPickupColor = 4
            else:
                teleGroundPickupColor = 5
            
            teleGroundPickupList.append(teleGroundPickupValue)
        
            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleGroundPickupDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleGroundPickupValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleGroundPickupColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(teleGroundPickupList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(teleGroundPickupList), 1))
        
    return rsCEA
