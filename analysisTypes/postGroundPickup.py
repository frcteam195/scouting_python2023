import statistics

# Note: This was changed to teleOP for CT Champs, but leaving the post in the name for simplicity
#       also changed to a simple numberic value. DB changed to insert a zero by defaut

#import mysql.connector
def postGroundPickup(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 21
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    postGroundPickupList = []
    
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
            postGroundPickup = matchResults[analysis.columns.index('postGroundPickup')]

            if postGroundPickup is None:
                postGroundPickup = 0
                
            postGroundPickupDisplay = str(postGroundPickup)
            postGroundPickupValue = postGroundPickup
            
            if postGroundPickup == 0:
                postGroundPickupColor = 1
            elif postGroundPickup <= 2:
                postGroundPickupColor = 2
            elif postGroundPickup <= 4:
                postGroundPickupColor = 3
            elif postGroundPickup <= 6:
                postGroundPickupColor = 4
            else:
                postGroundPickupColor = 5
            
            postGroundPickupList.append(postGroundPickupValue)
        
            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postGroundPickupDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postGroundPickupValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postGroundPickupColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postGroundPickupList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(postGroundPickupList), 1))
        
    return rsCEA
