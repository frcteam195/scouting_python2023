CREATE TABLE IF NOT EXISTS dev1.CEanalysisGraphs (
	team VARCHAR(10) NOT NULL,
	eventID INT NOT NULL,
	teleLowMean FLOAT NULL,
	teleLowMedian FLOAT NULL,
	teleLowFormat INT NULL,
	teleMidMean FLOAT NULL,
	teleMidMedian FLOAT NULL,
	teleMidFormat INT NULL,
	teleHighMean FLOAT NULL,
	teleHighMedian FLOAT NULL,
	teleHighFormat INT NULL,
	teleTotalMean FLOAT NULL,
	teleTotalMedian FLOAT NULL,
	teleTotalFormat INT NULL,
	autoRampMean FLOAT NULL,
	autoRampMedian FLOAT NULL,
	autoRampFormat INT NULL,
	autoGamePiecesMean FLOAT NULL,
	autoGamePiecesMedian FLOAT NULL,
	autoGamePiecesFormat INT NULL,
	autoScoreMean FLOAT NULL,
	autoScoreMedian FLOAT NULL,
	autoScoreFormat INT NULL,
	teleCommunityMean FLOAT NULL,
	teleCommunityMedian FLOAT NULL,
	teleCommunityFormat INT NULL,
	teleLZPickupMean FLOAT NULL,
	teleLZPickupMedian FLOAT NULL,
	teleLZPickupFormat INT NULL,
	rampMean FLOAT NULL,
	rampMedian FLOAT NULL,
	rampFormat INT NULL,
	teleScoreMean FLOAT NULL,
	teleScoreMedian FLOAT NULL,
	teleScoreFormat INT NULL,
	totalScoreMean FLOAT NULL,
	totalScoreMedian FLOAT NULL,
	totalScoreFormat FLOAT NULL,
	/* add more once we determine analysisTypes */
    PRIMARY KEY (team, eventID),
    FOREIGN KEY (team, eventID) REFERENCES teams (team, eventID)
) Engine = InnoDB;