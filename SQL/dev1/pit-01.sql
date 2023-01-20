CREATE TABLE IF NOT EXISTS dev1.pit (
        team VARCHAR(10) NOT NULL,
        BAeventID VARCHAR(20) NOT NULL,
        driveTypeID INT NULL,
        /* add pit columns here based on data modeling document */
        PRIMARY KEY(team),
        FOREIGN KEY (team) REFERENCES teams (team) ON DELETE CASCADE,
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
        FOREIGN KEY (driveTypeID) REFERENCES driveTypes (id) ON DELETE CASCADE
) Engine = InnoDB;
