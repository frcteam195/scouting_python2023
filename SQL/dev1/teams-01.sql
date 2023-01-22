CREATE TABLE IF NOT EXISTS dev1.teams (
        team VARCHAR(10),
        eventID INT,
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        teamCity VARCHAR(50),
        teamStateProv VARCHAR(50),
        teamCountry VARCHAR(50),
        PRIMARY KEY (team),
        FOREIGN KEY (eventID) REFERENCES events (id),
        FOREIGN KEY (team) REFERENCES teamsAll (team)
) Engine = InnoDB;
