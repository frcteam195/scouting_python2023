CREATE TABLE IF NOT EXISTS dev1.matchScouting (
        id INT AUTO_INCREMENT NOT NULL,
        BAeventID VARCHAR(20) NOT NULL,
        matchID INT NOT NULL,
        scouterID INT NULL,
        scoutingStatus INT NULL,
        team VARCHAR(10) NOT NULL,
        teamMatchNum INT NULL,
        allianceStationID INT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (matchID) REFERENCES matches (id) ON DELETE CASCADE
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE
) Engine = InnoDB;
