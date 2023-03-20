CREATE TABLE IF NOT EXISTS dev1.teamsAll (
        team VARCHAR(10),
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        teamCity VARCHAR(50) NULL,
        teamStateProv VARCHAR(50),
        teamCountry VARCHAR(50),
        PRIMARY KEY (team)
) Engine = InnoDB;
