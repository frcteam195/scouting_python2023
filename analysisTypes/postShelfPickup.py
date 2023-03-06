import statistics
#import mysql.connector
def postShelfPickup(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 20
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    postShelfPickupList = []
    
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
            
            postShelfPickup = matchResults[analysis.columns.index('postShelfPickup')]
            
            if postShelfPickup is None:
                postShelfPickupDisplay = 999
                postShelfPickupValue = 999
            elif postShelfPickup == 0:
                postShelfPickupDisplay = 'N'
                postShelfPickupValue = 0
                postShelfPickupColor = 2
            else:
                postShelfPickupDisplay = 'Y'
                postShelfPickupValue = 1
                postShelfPickupColor = 4
            
            postShelfPickupList.append(postShelfPickupValue)

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postShelfPickupDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postShelfPickupValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postShelfPickupColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postShelfPickupList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(postShelfPickupList), 1))

    return rsCEA
