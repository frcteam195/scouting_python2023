CREATE TABLE IF NOT EXISTS dev1.watch2 (
        sortOrder INT NOT NULL,
        team VARCHAR(10),
        PRIMARY KEY (sortOrder),
        FOREIGN KEY (team) REFERENCES teams (team)
) Engine = InnoDB;