import numpy as np

def scorePredMatchAlgorithm(redAllianceData, blueAllianceData):
    
    red1AutoPts, red2AutoPts, red3AutoPts = [t[1] for t in redAllianceData]
    red1AutoPtsStd, red2AutoPtsStd, red3AutoPtsStd = [t[2] for t in redAllianceData]
    red1AutoRampPts, red2AutoRampPts, red3AutoRampPts = [t[3] for t in redAllianceData]
    red1AutoRampPtsStd, red2AutoRampPtsStd, red3AutoRampPtsStd = [t[4] for t in redAllianceData]
    red1TelePts, red2TelePts, red3TelePts = [t[5] for t in redAllianceData]
    red1TelePtsStd, red2TelePtsStd, red3TelePtsStd = [t[6] for t in redAllianceData]
    red1EndgamePts, red2EndgamePts, red3EndgamePts = [t[7] for t in redAllianceData]
    red1EndgamePtsStd, red2EndgamePtsStd, red3EndgamePtsStd = [t[8] for t in redAllianceData]
    
    blue1AutoPts, blue2AutoPts, blue3AutoPts = [t[1] for t in blueAllianceData]
    blue1AutoPtsStd, blue2AutoPtsStd, blue3AutoPtsStd = [t[2] for t in blueAllianceData]
    blue1AutoRampPts, blue2AutoRampPts, blue3AutoRampPts = [t[3] for t in blueAllianceData]
    blue1AutoRampPtsStd, blue2AutoRampPtsStd, blue3AutoRampPtsStd = [t[4] for t in blueAllianceData]
    blue1TelePts, blue2TelePts, blue3TelePts = [t[5] for t in blueAllianceData]
    blue1TelePtsStd, blue2TelePtsStd, blue3TelePtsStd = [t[6] for t in blueAllianceData]
    blue1EndgamePts, blue2EndgamePts, blue3EndgamePts = [t[7] for t in blueAllianceData]
    blue1EndgamePtsStd, blue2EndgamePtsStd, blue3EndgamePtsStd = [t[8] for t in blueAllianceData]

    # calculate distributions from CEanalysisGraph means and stdev
    iter = 1000

    red1AutoPtsDist = np.random.normal(loc=red1AutoPts, scale=red1AutoPtsStd, size=iter)
    red2AutoPtsDist = np.random.normal(loc=red2AutoPts, scale=red2AutoPtsStd, size=iter)
    red3AutoPtsDist = np.random.normal(loc=red3AutoPts, scale=red3AutoPtsStd, size=iter)
    blue1AutoPtsDist = np.random.normal(loc=blue1AutoPts, scale=blue1AutoPtsStd, size=iter)
    blue2AutoPtsDist = np.random.normal(loc=blue2AutoPts, scale=blue2AutoPtsStd, size=iter)
    blue3AutoPtsDist = np.random.normal(loc=blue3AutoPts, scale=blue3AutoPtsStd, size=iter)
    redSumAutoPtsDist = red1AutoPtsDist + red2AutoPtsDist + red3AutoPtsDist
    blueSumAutoPtsDist = blue1AutoPtsDist + blue2AutoPtsDist + blue3AutoPtsDist

    red1AutoRampPtsDist = np.random.normal(loc=red1AutoRampPts, scale=red1AutoRampPtsStd, size=iter)
    red2AutoRampPtsDist = np.random.normal(loc=red2AutoRampPts, scale=red2AutoRampPtsStd, size=iter)
    red3AutoRampPtsDist = np.random.normal(loc=red3AutoRampPts, scale=red3AutoRampPtsStd, size=iter)
    blue1AutoRampPtsDist = np.random.normal(loc=blue1AutoRampPts, scale=blue1AutoRampPtsStd, size=iter)
    blue2AutoRampPtsDist = np.random.normal(loc=blue2AutoRampPts, scale=blue2AutoRampPtsStd, size=iter)
    blue3AutoRampPtsDist = np.random.normal(loc=blue3AutoRampPts, scale=blue3AutoRampPtsStd, size=iter)
    redSumAutoRampPtsDist = red1AutoRampPtsDist + red2AutoRampPtsDist + red3AutoRampPtsDist
    redSumAutoRampPtsDist[redSumAutoRampPtsDist > 12] =  12
    blueSumAutoRampPtsDist = blue1AutoRampPtsDist + blue2AutoRampPtsDist + blue3AutoRampPtsDist
    blueSumAutoRampPtsDist[blueSumAutoRampPtsDist > 12] =  12

    red1TelePtsDist = np.random.normal(loc=red1TelePts, scale=red1TelePtsStd, size=iter)
    red2TelePtsDist = np.random.normal(loc=red2TelePts, scale=red2TelePtsStd, size=iter)
    red3TelePtsDist = np.random.normal(loc=red3TelePts, scale=red3TelePtsStd, size=iter)
    blue1TelePtsDist = np.random.normal(loc=blue1TelePts, scale=blue1TelePtsStd, size=iter)
    blue2TelePtsDist = np.random.normal(loc=blue2TelePts, scale=blue2TelePtsStd, size=iter)
    blue3TelePtsDist = np.random.normal(loc=blue3TelePts, scale=blue3TelePtsStd, size=iter)
    redSumTelePtsDist = red1TelePtsDist + red2TelePtsDist + red3TelePtsDist
    blueSumTelePtsDist = blue1TelePtsDist + blue2TelePtsDist + blue3TelePtsDist

    red1EndgamePtsDist = np.random.normal(loc=red1EndgamePts, scale=red1EndgamePtsStd, size=iter)
    red2EndgamePtsDist = np.random.normal(loc=red2EndgamePts, scale=red2EndgamePtsStd, size=iter)
    red3EndgamePtsDist = np.random.normal(loc=red3EndgamePts, scale=red3EndgamePtsStd, size=iter)
    blue1EndgamePtsDist = np.random.normal(loc=blue1EndgamePts, scale=blue1EndgamePtsStd, size=iter)
    blue2EndgamePtsDist = np.random.normal(loc=blue2EndgamePts, scale=blue2EndgamePtsStd, size=iter)
    blue3EndgamePtsDist = np.random.normal(loc=blue3EndgamePts, scale=blue3EndgamePtsStd, size=iter)
    redSumEndgamePtsDist = red1EndgamePtsDist + red2EndgamePtsDist + red3EndgamePtsDist
    blueSumEndgamePtsDist = blue1EndgamePtsDist + blue2EndgamePtsDist + blue3EndgamePtsDist
    
    # finally calculate the alliance score distributions and means
    redScoreDist = redSumAutoPtsDist + redSumAutoRampPtsDist + redSumTelePtsDist + redSumEndgamePtsDist
    blueScoreDist = blueSumAutoPtsDist + blueSumAutoRampPtsDist + blueSumTelePtsDist + blueSumEndgamePtsDist
    # redPredScore = round(np.mean(redScoreDist))
    # bluePredScore = round(np.mean(blueScoreDist))
   
    redWins = (redScoreDist > blueScoreDist).sum()
    redWinProb = round((redWins / iter) * 100, 1)
    blueWinProb = round(100 - redWinProb, 1)

    return[redWinProb, blueWinProb]
