CREATE TABLE IF NOT EXISTS dev1.pit (
        team VARCHAR(10),
        BAeventID VARCHAR(20),
        driveType VARCHAR(20),
        PRIMARY KEY(team),
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
        FOREIGN KEY (team) REFERENCES CEteams (team) ON DELETE CASCADE
) Engine = InnoDB;
