import statistics

def goodOffBot(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 37
    goodOffBotList = []
    numberOfMatchesPlayed = 0
    count = 0

    print(f"2. {rsRobotL2MatchData}")
    if rsRobotL2MatchData == 0:
        rsCEA = {}
        return rsCEA
    else:
        for matchResults in rsRobotL2MatchData:
            team = matchResults[analysis.L2Columns.index('team')]
            rsCEA['team'] = team
            rsCEA['eventID'] = matchResults[analysis.L2Columns.index('eventID')]
            preNoShow = matchResults[analysis.L2Columns.index('preNoShow')]
            scoutingStatus = matchResults[analysis.L2Columns.index('scoutingStatus')]
            if preNoShow == 1:
                rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'D'] = 'DNS'
            elif scoutingStatus == 2:
                rsCEA['M' + str(matchResults[analysis.L2Columns.index('teamMatchNum')]) + 'D'] = 'UR'
            else:
                goodOffBot = matchResults[analysis.L2Columns.index('goodOffBot')]
                if goodOffBot is None:
                    display = '999'
                    value = 0
                    format = 2
                elif goodOffBot == 0:
                    display = 'N'
                    value = 0
                    format = 3
                    count += 1
                    goodOffBotList.append(value)
                elif goodOffBot == 1:
                    display = 'Y'
                    value = 1
                    format = 4
                    count += 1
                    goodOffBotList.append(value)
                elif goodOffBot == 2:
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
                rsCEA['S1V'] = round(statistics.mean(goodOffBotList), 1)
                rsCEA['S1D'] = str(round(statistics.mean(goodOffBotList), 1))
                rsCEA['S2V'] = round(statistics.median(goodOffBotList), 1)
                rsCEA['S2D'] = str(round(statistics.median(goodOffBotList), 1))
            else:
                rsCEA['S1V'] = 0
                rsCEA['S1D'] = ''
                rsCEA['S2V'] = 0
                rsCEA['S2D'] = ''

        return rsCEA
