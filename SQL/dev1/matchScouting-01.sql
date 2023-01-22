CREATE TABLE IF NOT EXISTS dev1.matchScouting (
        id INT AUTO_INCREMENT NOT NULL,
        eventID INT NOT NULL,
        matchID INT NOT NULL,
        matchNum INT NULL,
        scouterID INT NULL,
        scoutingStatus INT NULL,
        team VARCHAR(10) NOT NULL,
        teamMatchNum INT NULL,
        scoutingRoleID INT NULL,
        preStartPos TINYINT NULL,
        /* add Level 1 columns here */
        /* add Level 2 columns here. Note that these columns must match those of the level2 DB table */
        PRIMARY KEY (id),
        FOREIGN KEY (eventID) REFERENCES events (id),
        FOREIGN KEY (matchID) REFERENCES matches (id),
        FOREIGN KEY (scouterID) REFERENCES scouters (id),
        FOREIGN KEY (team) REFERENCES teams (team),
        FOREIGN KEY (scoutingRoleID) REFERENCES scoutingRoles (id)
) Engine = InnoDB;
