CREATE TABLE IF NOT EXISTS dev1.BAoprs (
	eventID INT NOT NULL,
	team VARCHAR(10) NOT NULL,
	OPR FLOAT NULL,
	PRIMARY KEY(team),
	FOREIGN KEY (team, eventID) REFERENCES teams (team, eventID)
) Engine = InnoDB;
