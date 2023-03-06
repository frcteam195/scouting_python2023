import statistics
#import mysql.connector
def postGoodPartner(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 22
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    postGoodPartnerList = []
    
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
            
            postGoodPartner = matchResults[analysis.columns.index('postGoodPartner')]
            
            if postGoodPartner is None:
                postGoodPartnerDisplay = '999'
            elif postGoodPartner == 0:
                postGoodPartnerDisplay = 'N'
                postGoodPartnerValue = 0
                postGoodPartnerColor = 2
            else:
                postGoodPartnerDisplay = 'Y'
                postGoodPartnerValue = 1
                postGoodPartnerColor = 4

            postGoodPartnerList.append(postGoodPartnerValue)

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postGoodPartnerDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postGoodPartnerValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postGoodPartnerColor

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postGoodPartnerList), 1)
        rsCEA['S1D'] = str(round(statistics.mean(postGoodPartnerList), 1))
   
    return rsCEA