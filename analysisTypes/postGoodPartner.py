import statistics
#import mysql.connector
def postGoodPartner(analysis, rsRobotMatchData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 22
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    postGoodPartnerList = []
    
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
            
            postGoodPartner = matchResults[analysis.columns.index('postGoodPartner')]
            
            
            if postGoodPartner is None:
                postGoodPartner = 0
            

            postGoodPartnerDisplay = postGoodPartner
            postGoodPartnerValue = postGoodPartner
            
            if postGoodPartner == 1:
                postGoodPartnerColor = 4
            elif postGoodPartner == 0:
                postGoodPartnerColor = 2
            
           
            

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postGoodPartnerDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postGoodPartnerValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postGoodPartnerColor

            postGoodPartnerList.append(postGoodPartnerValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postGoodPartnerList), 1)
    return rsCEA