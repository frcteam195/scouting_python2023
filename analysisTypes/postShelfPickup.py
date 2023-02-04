import statistics
#import mysql.connector
def postShelfPickup(analysis, rsRobotMatchData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 20
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    postShelfPickupList = []
    
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
            
            postShelfPickup = matchResults[analysis.columns.index('postShelfPickup')]
            
            
            if postShelfPickup is None:
                postShelfPickup = 0
            

            postShelfPickupDisplay = postShelfPickup
            postShelfPickupValue = postShelfPickup
            
            if postShelfPickup == 1:
                postShelfPickupColor = 4
            elif postShelfPickup == 0:
                postShelfPickupColor = 2
            
           
            

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postShelfPickupDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postShelfPickupValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postShelfPickupColor

            postShelfPickupList.append(postShelfPickupValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postShelfPickupList), 1)
    return rsCEA