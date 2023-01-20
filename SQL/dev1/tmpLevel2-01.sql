CREATE TABLE IF NOT EXISTS dev1.tmpLevel2 (
        BAeventID VARCHAR(20) NOT NULL,
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
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
        FOREIGN KEY (matchID) REFERENCES matches (id) ON DELETE CASCADE,
        FOREIGN KEY (scouterID) REFERENCES scouters (id) ON DELETE CASCADE,
        FOREIGN KEY (team) REFERENCES teams (team) ON DELETE CASCADE,
        FOREIGN KEY (scoutingRoleID) REFERENCES scoutingRole (id) ON DELETE CASCADE
) Engine = InnoDB;
