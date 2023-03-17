import statistics

def L2questions(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 30 
    numberOfMatchesPlayed = 0

    dict = {30: 'speed', 
            31: 'maneuverability', 
            32: 'sturdiness', 
            33: 'climb', 
            34: 'effort', 
            35: 'scoringEff', 
            36: 'intakeEff'}
    # print(dict)

    # Values 0 0 5 with 0 = N/A, 1 being poor and 5 being the best

    for L2matchResults in rsRobotL2MatchData:
        team = L2matchResults[analysis.L2Columns.index('team')]
        preNoShow = L2matchResults[analysis.L2Columns.index('preNoShow')]
        eventID = L2matchResults[analysis.L2Columns.index('eventID')]
        scoutingStatus = L2matchResults[analysis.L2Columns.index('scoutingStatus')]
        teamMatchNum = L2matchResults[analysis.L2Columns.index('teamMatchNum')]

        rsCEA['team'] = team
        rsCEA['eventID'] = eventID
        
        if preNoShow == 1:
            rsCEA['M' + str(teamMatchNum) + 'D'] = 'DNS'
        elif scoutingStatus == 2:
            rsCEA['M' + str(teamMatchNum) + 'D'] = 'UR'
        else:
            for analysisTypeID in dict:
                analysisType = dict[analysisTypeID]
                analysisTypeValue = L2matchResults[analysis.L2Columns.index(analysisType)]
                print(f"analysisTypeID = {analysisTypeID}, analysisType = {analysisType}, analysisTypeValue = {analysisTypeValue}")
                rsCEA['M' + teamMatchNum + 'D'] = analysisTypeValue
            # print(f"team = {team}, teamMatchNum = {teamMatchNum}, speed = {speed}, {maneuverability}, {sturdiness}, {climb}, {effort}, {scoringEff}, {intakeEff}")

            numberOfMatchesPlayed += 1
            rsCEA['M' + str(L2matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'D'] = '99'
            # rsCEA['M' + str(L2matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = L2matchResults[
            #     analysis.columns.index('preStartPos')]

    return rsCEA