import statistics

def goodDefBot(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 38
    goodDefBotList = []
    numberOfMatchesPlayed = 0
    count = 0

    for matchResults in rsRobotL2MatchData:
        rsCEA['team'] = matchResults[analysis.L2Columns.index('team')]
        rsCEA['eventID'] = matchResults[analysis.L2Columns.index('eventID')]
        preNoShow = matchResults[analysis.L2Columns.index('preNoShow')]
        scoutingStatus = matchResults[analysis.L2Columns.index('scoutingStatus')]
        if preNoShow == 1:
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'D'] = 'DNS'
        elif scoutingStatus == 2:
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'D'] = 'UR'
        else:
            goodDefBot = matchResults[analysis.L2Columns.index('goodDefBot')]
            if goodDefBot is None:
                display = '999'
                value = 0
                format = 2
            elif goodDefBot == 0:
                display = 'N'
                value = 0
                format = 3
                count += 1
                goodDefBotList.append(value)
            elif goodDefBot == 1:
                display = 'Y'
                value = 1
                format = 4
                count += 1
                goodDefBotList.append(value)
            elif goodDefBot == 2:
                display = 'NA'
                value = 0
                format = 0
            else:
                display = '888'
                value = 0
                format = 2
            
            numberOfMatchesPlayed += 1

            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'D'] = display
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'V'] = value
            rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'F'] = format
        
    if numberOfMatchesPlayed > 0:
        if count > 0:
            rsCEA['S1V'] = round(statistics.mean(goodDefBotList), 1)
            rsCEA['S1D'] = str(round(statistics.mean(goodDefBotList), 1))
            rsCEA['S2V'] = round(statistics.median(goodDefBotList), 1)
            rsCEA['S2D'] = str(round(statistics.median(goodDefBotList), 1))
        else:
                rsCEA['S1V'] = 0
                rsCEA['S1D'] = '-'
                rsCEA['S2V'] = 0
                rsCEA['S2D'] = '-'

    return rsCEA
