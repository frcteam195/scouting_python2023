import statistics

def startingPositionTest(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    startingPositionList = []
    totalMatchesPlayed = len(rsRobotMatchData)

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
        rsCEA['analysisTypeID'] = 1 
        rsCEA['eventID'] = matchResults[analysis.columns.index('eventID')]
        # We are hijacking the starting position to write DNS or UR. This should go to Auto as it will not
        #   likely be displayed on team picker pages.
        # autoDidNotShow = matchResults[analysis.columns.index('autoDidNotShow')]
        autoDidNotShow = 0   # temporarily adding this to make it work, fix later !!!
        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if autoDidNotShow == 1:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'DNS'
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = 'Null'
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = 'Null'
        elif scoutingStatus == 2:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'UR'
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = 'Null'
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = 'Null'
        else:
            preStartPos = matchResults[analysis.columns.index('preStartPos')]
            if preStartPos is None:
                preStartPos = 0

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = matchResults[
                analysis.columns.index('preStartPos')]
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = 0
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = matchResults[
                analysis.columns.index('preStartPos')]
            
            startingPositionList.append(preStartPos)
    
    # Set all matches not played to 'Null' values
    if totalMatchesPlayed < 12:
        i = totalMatchesPlayed + 1
        print(f"i = {i}")
        while i <= 12:
            rsCEA['M' + str(i) + 'D'] = 'Null'
            rsCEA['M' + str(i) + 'F'] = 'Null'
            rsCEA['M' + str(i) + 'V'] = 'Null'
            i += 1

    rsCEA['S1D'] = 'Null'
    rsCEA['S1F'] = 'Null'
    
    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(startingPositionList), 1)
    else:
        rsCEA['S1V'] = 'Null'
    # define all the other Summary values
    rsCEA['S2D'] = 'Null'
    rsCEA['S2F'] = 'Null'
    rsCEA['S2V'] = 'Null'
    rsCEA['S3D'] = 'Null'
    rsCEA['S3F'] = 'Null'
    rsCEA['S3V'] = 'Null'
    rsCEA['S4D'] = 'Null'
    rsCEA['S4F'] = 'Null'
    rsCEA['S4V'] = 'Null'
    rsCEA['Min'] = 'Null'
    rsCEA['Max'] = 'Null'
    rsCEA['Per'] = 'Null'
    
    return rsCEA