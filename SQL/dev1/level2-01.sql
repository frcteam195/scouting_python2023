CREATE TABLE IF NOT EXISTS dev1.level2 (
        eventID INT NOT NULL,
        matchID INT NOT NULL,
        matchNum INT NULL,
        scouterID INT NULL,
        scoutingStatus INT NULL,
        synced2MS BOOLEAN DEFAULT false,
        team VARCHAR(10) NOT NULL,
        teamMatchNum INT NULL,
        scoutingRoleID INT NULL,
        /* add Level 2 columns here. Note that these columns must match those of the matchScouting DB table */
        PRIMARY KEY (matchID),
        FOREIGN KEY (eventID) REFERENCES events (id),
        FOREIGN KEY (matchID) REFERENCES matches (id),
        FOREIGN KEY (scouterID) REFERENCES scouters (id),
        FOREIGN KEY (team) REFERENCES teams (team),
        FOREIGN KEY (scoutingRoleID) REFERENCES scoutingRoles (id)
) Engine = InnoDB;
