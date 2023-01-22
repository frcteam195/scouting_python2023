CREATE TABLE IF NOT EXISTS dev1.watch1 (
        sortOrder INT NOT NULL,
        team VARCHAR(10),
        eventID INT,
        PRIMARY KEY (team, eventID, sortOrder),
        FOREIGN KEY (team) REFERENCES teams (team),
        FOREIGN KEY (eventID) REFERENCES events (id)   
) Engine = InnoDB;
