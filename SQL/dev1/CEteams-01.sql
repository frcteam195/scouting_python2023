CREATE TABLE IF NOT EXISTS dev1.CEteams (
        team VARCHAR(10),
        BAeventID VARCHAR(20),
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        teamCity VARCHAR(50),
        teamStateProv VARCHAR(50),
        teamCountry VARCHAR(50),
        PRIMARY KEY(team),
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
        FOREIGN KEY (team) REFERENCES teams (team) ON DELETE CASCADE
) Engine = InnoDB;
