import statistics

# Note: This was changed to teleOP for CT Champs, but leaving the post in the name for simplicity
#       also changed to a simple numberic value. DB changed to insert a zero by defaut

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
                postShelfPickup = 0
                
            postShelfPickupDisplay = str(postShelfPickup)
            postShelfPickupValue = postShelfPickup
            
            if postShelfPickup == 0:
                postShelfPickupColor = 1
            elif postShelfPickup <= 2:
                postShelfPickupColor = 2
            elif postShelfPickup <= 4:
                postShelfPickupColor = 3
            elif postShelfPickup <= 6:
                postShelfPickupColor = 4
            else:
                postShelfPickupColor = 5

            postShelfPickupList.append(postShelfPickup)

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postShelfPickupDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postShelfPickupValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postShelfPickupColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postShelfPickupList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(postShelfPickupList), 1))

    return rsCEA
