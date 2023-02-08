CREATE TABLE IF NOT EXISTS dev1.CEanalysisGraphs (
	CEanalysisGraphsID INT NOT NULL,
	team VARCHAR(10) NOT NULL,
	eventID INT NOT NULL,
	teleLowMean FLOAT NULL,
	teleLowMedian FLOAT NULL,
	teleMidMean FLOAT NULL,
	teleMidMedian FLOAT NULL,
	teleHighMean FLOAT NULL,
	teleHighMedian FLOAT NULL,
	/* add more once we determine analysisTypes */
    PRIMARY KEY (CEanalysisGraphsID),
    FOREIGN KEY (eventID) REFERENCES events (eventID),
    FOREIGN KEY (team) REFERENCES teams (team)
) Engine = InnoDB;