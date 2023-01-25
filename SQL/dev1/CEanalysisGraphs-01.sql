CREATE TABLE IF NOT EXISTS dev1.CEanalysisGraphs (
	CEanalysisGraphsID INT NOT NULL,
	team VARCHAR(10) NOT NULL,
	eventID INT NOT NULL,
	/* list all the summary information for graphs by team
	   y-axis = value listed here, x-axis = team */
	autoMean FLOAT NULL,
	autoMedian FLOAT NULL,
	scoreMean FLOAT NULL,
	scoreMedian FLOAT NULL,
	/* add more once we determine analysisTypes */
    PRIMARY KEY (CEanalysisGraphsID),
    FOREIGN KEY (eventID) REFERENCES events (eventID),
    FOREIGN KEY (team) REFERENCES teams (team)
) Engine = InnoDB;