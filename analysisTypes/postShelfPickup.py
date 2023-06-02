import statistics
#import mysql.connector
def postShelfPickup(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 20
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    teleShelfPickupList = []
    
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
            
            teleShelfPickup = matchResults[analysis.columns.index('teleShelfPickup')]
            
            teleShelfPickupDisplay = str(postShelfPickup)
            teleShelfPickupValue = teleShelfPickup

            if teleShelfPickup == 0:
                teleShelfPickupColor = 1
            elif teleShelfPickup <= 2:
                teleShelfPickupColor = 2
            elif teleShelfPickup <= 4:
                teleShelfPickupColor = 3
            elif teleShelfPickup <= 6:
                teleShelfPickupColor = 4
            else:
                teleShelfPickupColor = 5
            
            teleShelfPickupList.append(teleShelfPickupValue)

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleShelfPickupDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = teleShelfPickupValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleShelfPickupColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(teleShelfPickupList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(teleShelfPickupList), 1))

    return rsCEA
