import statistics

from requests import post

def startingPosition(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 28
    numberOfMatchesPlayed = 0

    postTippedOverList = []

    # example for loading pit data into analysis
    # if rsRobotPitData == 0:
    #   # print("doing nothing")
    # else: 
    #     for pitResults in rsRobotPitData:
    #         width = pitResults[analysis.pitColumns.index('width')]

     # example for loading L2 data into analysis
    # if rsRobotL2MatchData == 0:
    #     #nprint("doing nothing")
    # else: 
    #     for L2Results in rsRobotL2MatchData:
    #         print(rsRobotL2MatchData)

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
            postTippedOver = matchResults[analysis.columns.index('postTippedOver')]
           
            
            
            if postTippedOver is None:
                postTippedOver = 0

                
            postTippedOverDisplay = postTippedOver
            postTippedOverValue = postTippedOver
            
            if postTippedOver == 1:
                postSubBrokeColor = 4
            elif postTippedOver == 0:
                postSubBrokeColor = 2

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = matchResults[
                analysis.columns.index('PostTippedOver')]
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = matchResults[
                analysis.columns.index('postTippedOver')]
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = 0
            postTippedOver.append(postTippedOver)

    if numberOfMatchesPlayed > 0:
        mean = round(statistics.mean(postTippedOverList), 1)
        median = round(statistics.median(postTippedOverList), 1)
        rsCEA['S1V'] = mean
        rsCEA['S1D'] = str(mean)
        if mean == 0:
            rsCEA['S1F'] = 2
        elif mean == 1:
            rsCEA['S1F'] = 4
        else:
            rsCEA['S1F'] = 999
        rsCEA['S2V'] = median
        rsCEA['S2D'] = str(median)
        if median == 0:
            rsCEA['S1F'] = 2
        elif median == 1:
            rsCEA['S1F'] = 4
        else:
            rsCEA['S1F'] = 999
    return rsCEA