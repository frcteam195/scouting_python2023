import statistics
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
        # We are hijacking the starting position to write DNS or UR. This should go to Auto as it will not
        #   likely be displayed on team picker pages.
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
            

            postGroundPickupDisplay = postGroundPickup
            postGroundPickupValue = postGroundPickup
            
            if postGroundPickup == 1:
                postGroundPickupColor = 4
            elif postGroundPickup == 0:
                postGroundPickupColor = 2
            
           
            

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postGroundPickupDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postGroundPickupValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postGroundPickupColor

            postGroundPickupList.append(postGroundPickupValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postGroundPickupList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(postGroundPickupList), 1))
        rsCEA['S2V'] = round(statistics.median(postGroundPickupList), 1)
        rsCEA['S2D'] = str(round(statistics.median(postGroundPickupList), 1))
    return rsCEA