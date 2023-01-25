CREATE TABLE IF NOT EXISTS dev1.teams (
        team VARCHAR(10),
        eventID INT,
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        PRIMARY KEY (team, eventID),
        FOREIGN KEY (eventID) REFERENCES events (eventID),
        FOREIGN KEY (team) REFERENCES teamsAll (team)
) Engine = InnoDB;
