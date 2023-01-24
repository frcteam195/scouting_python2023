CREATE TABLE IF NOT EXISTS dev1.matchScoutingL2 (
        id INT AUTO_INCREMENT NOT NULL,
        eventID INT NOT NULL,
        matchID INT NOT NULL,
        matchNum INT NULL,
        allianceStationID INT NULL,
        team VARCHAR(10) NOT NULL,
        teamMatchNum INT NULL,
        scoutingStatus INT NULL,
        scouterID INT NULL,
        synced2MS BOOLEAN DEFAULT false,
        /* add Level 2 columns here. Note that these columns must match those of the matchScouting DB table */
        PRIMARY KEY (id),
        FOREIGN KEY (eventID) REFERENCES events (id),
        FOREIGN KEY (matchID) REFERENCES matches (id),
        FOREIGN KEY (scouterID) REFERENCES scouters (id),
        FOREIGN KEY (team) REFERENCES teams (team),
        FOREIGN KEY (allianceStationID) REFERENCES allianceStations (id)
) Engine = InnoDB;
