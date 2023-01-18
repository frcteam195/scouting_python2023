CREATE TABLE IF NOT EXISTS dev1.CEteams (
        team VARCHAR(10),
        BAeventID VARCHAR(20),
        driveType VARCHAR(20),
        PRIMARY KEY(team),
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
        FOREIGN KEY (team) REFERENCES BAteams (team) ON DELETE CASCADE
) Engine = InnoDB;
