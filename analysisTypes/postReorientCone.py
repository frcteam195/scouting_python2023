import statistics
#import mysql.connector
def postReorientCone(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 19
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    postReorientConeList = []
    
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
            
            postReorientCone = matchResults[analysis.columns.index('postReorientCone')]
            
            
            if postReorientCone is None:
                postReorientCone = 0
            

            postReorientConeDisplay = postReorientCone
            postReorientConeValue = postReorientCone
            
            if postReorientCone == 1:
                postReorientConeColor = 4
            elif postReorientCone == 0:
                postReorientConeColor = 2
            
           
            

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postReorientConeDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postReorientConeValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postReorientConeColor

            postReorientConeList.append(postReorientConeValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postReorientConeList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(postReorientConeList), 1))
        rsCEA['S2V'] = round(statistics.median(postReorientConeList), 1)
        rsCEA['S2D'] = str(round(statistics.median(postReorientConeList), 1))
    return rsCEA