CREATE TABLE IF NOT EXISTS dev1.BA_CEteams (
        team VARCHAR(10),
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        teamCity VARCHAR(50) NULL,
        teamStateProv VARCHAR(50),
        teamCountry VARCHAR(50),
        PRIMARY KEY (team),
        FOREIGN KEY (team) REFERENCES teamsAll (team)
) Engine = InnoDB;