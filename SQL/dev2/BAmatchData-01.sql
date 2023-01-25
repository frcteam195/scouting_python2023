CREATE TABLE IF NOT EXISTS dev2.BAmatchData (
	matchNum INT NOT NULL,
	eventID INT,
	matchTime VARCHAR(20) NULL,
	actualTime VARCHAR(20) NULL,
	red1 INT NULL,
	red2 INT NULL,
	red3 INT NULL,
	blue1 INT NULL,
	blue2 INT NULL,
	blue3 INT NULL,
	redScore INT NULL,
	blueScore INT NULL,
	/* add additional entries as described in the BA API once it is released for Charged Up */
	PRIMARY KEY (matchNum),
    FOREIGN KEY (eventID) REFERENCES events (eventID)
) Engine = InnoDB;