import statistics

def autoRamp(analysis, rsRobotMatchData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 4
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    autoRampList = []

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

            autoRamp = matchResults[analysis.columns.index('autoRamp')]

            numGamePieces = 0
            score1 = matchResults[analysis.columns.index('autoScore1')]
            score2 = matchResults[analysis.columns.index('autoScore2')]
            score3 = matchResults[analysis.columns.index('autoScore3')]
            score4 = matchResults[analysis.columns.index('autoScore4')]

            mb = ""
            autoMB = matchResults[analysis.columns.index('autoMB')]

            if score1 > 0:
                numGamePieces += 1
            if score2 > 0:
                numGamePieces += 1
            if score3 > 0:
                numGamePieces += 1
            if score4 > 0:
                numGamePieces += 1

            if autoMB > 0:
                mb = "*"
                
            if autoRamp == 0: #No Attempt
                autoRampDisplay = "0|" + str(numGamePieces) + mb
                autoRampValue = 0

                if numGamePieces == 0:
                    autoRampColor = 1 #Black
                else: #with move bonus or piece placement
                    autoRampColor = 0 #White   

            elif autoRamp == 1: #Failed Attempt
                autoRampDisplay = "0|" + str(numGamePieces) + mb
                autoRampValue = 0
                autoRampColor = 2 #Red

            elif autoRamp == 2: #Docked Not Engaged
                autoRampDisplay = "8|" + str(numGamePieces) + mb
                autoRampValue = 8
                autoRampColor = 3 #Yellow

            elif autoRamp == 3: #Docked And Engaged
                autoRampDisplay = "12|" + str(numGamePieces) + mb
                autoRampValue = 12

                if numGamePieces == 0:
                    autoRampColor = 4 #Green
                else: #with move bonus or piece placement
                    autoRampColor = 5 #Blue
            

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = autoRampDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = autoRampValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = autoRampColor

            autoRampList.append(autoRampValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(autoRampList), 1)

    return rsCEA