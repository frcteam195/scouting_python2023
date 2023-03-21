from re import T
import statistics

def teleWasObstructed(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 14

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
            wasObstructed = matchResults[analysis.columns.index('teleWasObstructed')]

            if wasObstructed == 0:
                teleWasObstructedDisplay = "N"
                teleWasObstructedColor = 6
            elif wasObstructed == 1:
                teleWasObstructedDisplay = "Y"
                teleWasObstructedColor = 7
            else:
                teleWasObstructedDisplay = "999"
            
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = teleWasObstructedDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = teleWasObstructedColor

    return rsCEA