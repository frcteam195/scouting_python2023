import numpy as np

def scorePredAllianceAlgorithm(allianceData):
    
    team1AutoPts, team2AutoPts, team3AutoPts = [t[1] for t in allianceData]
    team1AutoPtsStd, team2AutoPtsStd, team3AutoPtsStd = [t[2] for t in allianceData]
    team1AutoRampPts, team2AutoRampPts, team3AutoRampPts = [t[3] for t in allianceData]
    team1AutoRampPtsStd, team2AutoRampPtsStd, team3AutoRampPtsStd = [t[4] for t in allianceData]
    team1TelePts, team2TelePts, team3TelePts = [t[5] for t in allianceData]
    team1TelePtsStd, team2TelePtsStd, team3TelePtsStd = [t[6] for t in allianceData]
    team1EndgamePts, team2EndgamePts, team3EndgamePts = [t[7] for t in allianceData]
    team1EndgamePtsStd, team2EndgamePtsStd, team3EndgamePtsStd = [t[8] for t in allianceData]
    
    # calculate distributions from CEanalysisGraph means and stdev
    iter = 1000

    team1AutoPtsDist = np.random.normal(loc=team1AutoPts, scale=team1AutoPtsStd, size=iter)
    team2AutoPtsDist = np.random.normal(loc=team2AutoPts, scale=team2AutoPtsStd, size=iter)
    team3AutoPtsDist = np.random.normal(loc=team3AutoPts, scale=team3AutoPtsStd, size=iter)
    allianceSumAutoPtsDist = team1AutoPtsDist + team2AutoPtsDist + team3AutoPtsDist

    team1AutoRampPtsDist = np.random.normal(loc=team1AutoRampPts, scale=team1AutoRampPtsStd, size=iter)
    team2AutoRampPtsDist = np.random.normal(loc=team2AutoRampPts, scale=team2AutoRampPtsStd, size=iter)
    team3AutoRampPtsDist = np.random.normal(loc=team3AutoRampPts, scale=team3AutoRampPtsStd, size=iter)
    allianceSumAutoRampPtsDist = team1AutoRampPtsDist + team2AutoRampPtsDist + team3AutoRampPtsDist
    allianceSumAutoRampPtsDist[allianceSumAutoRampPtsDist > 12] =  12

    team1TelePtsDist = np.random.normal(loc=team1TelePts, scale=team1TelePtsStd, size=iter)
    team2TelePtsDist = np.random.normal(loc=team2TelePts, scale=team2TelePtsStd, size=iter)
    team3TelePtsDist = np.random.normal(loc=team3TelePts, scale=team3TelePtsStd, size=iter)
    allianceSumTelePtsDist = team1TelePtsDist + team2TelePtsDist + team3TelePtsDist

    team1EndgamePtsDist = np.random.normal(loc=team1EndgamePts, scale=team1EndgamePtsStd, size=iter)
    team2EndgamePtsDist = np.random.normal(loc=team2EndgamePts, scale=team2EndgamePtsStd, size=iter)
    team3EndgamePtsDist = np.random.normal(loc=team3EndgamePts, scale=team3EndgamePtsStd, size=iter)
    allianceSumEndgamePtsDist = team1EndgamePtsDist + team2EndgamePtsDist + team3EndgamePtsDist
    
    # finally calculate the alliance score distributions and means
    allianceScoreDist = allianceSumAutoPtsDist + allianceSumAutoRampPtsDist + allianceSumTelePtsDist + allianceSumEndgamePtsDist
    alliancePredScore = round(np.mean(allianceScoreDist))

    return alliancePredScore
