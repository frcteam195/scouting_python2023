CREATE TABLE IF NOT EXISTS dev1.watch1 (
        sortOrder INT NOT NULL,
        team VARCHAR(10),
        BAeventID VARCHAR(20),
        PRIMARY KEY (team, BAeventID, sortOrder),
        FOREIGN KEY (team) REFERENCES teams (team) ON DELETE CASCADE,
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE    
) Engine = InnoDB;
