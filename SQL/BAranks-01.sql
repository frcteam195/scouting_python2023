CREATE TABLE IF NOT EXISTS dev1.BAranks(
	eventID INT NOT NULL,
	team VARCHAR(10) NULL,
	rank INT NULL,
	PRIMARY KEY (team),
	FOREIGN KEY (team, eventID) REFERENCES teams (team, eventID)
) Engine = InnoDB;
