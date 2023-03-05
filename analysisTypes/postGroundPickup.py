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
        
        preNoShow = matchResults[analysis.columns.index('preNoShow')]
        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if preNoShow == 1:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'DNS'
        elif scoutingStatus == 2:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'UR'
        else:
            postGroundPickup = matchResults[analysis.columns.index('postGroundPickup')]
            
            if postGroundPickup is None:
                postGroundPickupDisplay = 999
                postGroundPickupValue = 999
                postGroundPickupColor = 0
            elif postGroundPickup == 0:
                postGroundPickupDisplay = 'N'
                postGroundPickupValue = 0
                postGroundPickupColor = 2
            else:
                postGroundPickupDisplay = 'Y'
                postGroundPickupValue = 1
                postGroundPickupColor = 4
            
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
