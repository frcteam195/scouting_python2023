CREATE TABLE IF NOT EXISTS dev2.BArank(
	team VARCHAR(10) NULL,
	rank INT NULL,
	PRIMARY KEY (team),
	FOREIGN KEY (team) REFERENCES teams (team)
) Engine = InnoDB;