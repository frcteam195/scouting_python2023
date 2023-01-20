CREATE TABLE IF NOT EXISTS dev1.CEanalysisGraphs (
	id INT NOT NULL,
	team VARCHAR(10) NOT NULL,
	BAeventID VARCHAR(20) NOT NULL,
	/* list all the summary information for graphs by team
	   y-axis = value listed here, x-axis = team */
	autoMean FLOAT NULL,
	autoMedian FLOAT NULL,
	scoreMean FLOAT NULL,
	scoreMedian FLOAT NULL,
	/* add more once we determine analysisTypes */
    PRIMARY KEY (id),
    FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
    FOREIGN KEY (team) REFERENCES teams (team) ON DELETE CASCADE
) Engine = InnoDB;