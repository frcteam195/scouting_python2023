CREATE TABLE IF NOT EXISTS dev1.pit (
        team VARCHAR(10) NOT NULL,
        eventID INT NOT NULL,
        driveTypeID INT NULL,
        /* add pit columns here based on data modeling document */
        PRIMARY KEY(team),
        FOREIGN KEY (team) REFERENCES teams (team),
        FOREIGN KEY (eventID) REFERENCES events (id),
        FOREIGN KEY (driveTypeID) REFERENCES driveTypes (id)
) Engine = InnoDB;
