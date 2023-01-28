

def startingPosition(analysis, rsRobotMatchData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 1
    numberOfMatchesPlayed = 0

    # Loop through each match the robot played in.
    for matchResults in rsRobotMatchData:
        rsCEA['team'] = matchResults[analysis.columns.index('team')]
        rsCEA['eventID'] = matchResults[analysis.columns.index('eventID')]
        # We are hijacking the starting position to write DNS or UR. This should go to Auto as it will not
        #   likely be displayed on team picker pages.
        # autoDidNotShow = matchResults[analysis.columns.index('autoDidNotShow')]
        autoDidNotShow = 0   # temporarily adding this to make it work, fix later !!!
        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if autoDidNotShow == 1:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'DNS'
        elif scoutingStatus == 2:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'UR'
        else:
            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = matchResults[
                analysis.columns.index('preStartPos')]
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = matchResults[
                analysis.columns.index('preStartPos')]
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = 0

    return rsCEA