import statistics

def autoScore(analysis, rsRobotMatchData):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['analysisTypeID'] = 2
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
            
            score1 = matchResults[analysis.columns.index('autoScore1')]
            score2 = matchResults[analysis.columns.index('autoScore2')]
            score3 = matchResults[analysis.columns.index('autoScore3')]
            score4 = matchResults[analysis.columns.index('autoScore4')]
            totalscore = 0

            mb = ""
            autoMB = matchResults[analysis.columns.index('autoMB')]
            if autoMB > 0:
                mb = "*"


            if (score1 >= 1) and (score1 <= 9):
                totalscore += 6
            elif (score1 >= 10) and (score1 <= 18):
                totalscore += 4
            elif (score1 >= 19) and (score1 <= 27):
                totalscore += 6

            if (score2 >= 1) and (score2 <= 9):
                totalscore += 6
            elif (score2 >= 10) and (score2 <= 18):
                totalscore += 4
            elif (score2 >= 19) and (score2 <= 27):
                totalscore += 6

            if (score3 >= 1) and (score3 <= 9):
                totalscore += 6
            elif (score3 >= 10) and (score3 <= 18):
                totalscore += 4
            elif (score3 >= 19) and (score3 <= 27):
                totalscore += 6

            if (score4 >= 1) and (score4 <= 9):
                totalscore += 6
            elif (score4 >= 10) and (score4 <= 18):
                totalscore += 4
            elif (score4 >= 19) and (score4 <= 27):
                totalscore += 6
            
            autoScoreDisplay = str(totalscore) + mb
            autoScoreValue = totalscore
            
            if totalscore == 0:
                autoScoreColor = 1
            elif totalscore == 3:
                autoScoreColor = 2
            elif (totalscore >= 4) and (totalscore <= 6):
                autoScoreColor = 3
            elif (totalscore >= 7) and (totalscore <= 12):
                autoScoreColor = 4
            elif (totalscore > 12):
                autoScoreColor = 5

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = autoScoreDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = autoScoreValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = autoScoreColor

            autoRampList.append(autoScoreValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(autoRampList), 1)

    return rsCEA