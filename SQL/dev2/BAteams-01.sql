CREATE TABLE IF NOT EXISTS dev2.BAteams (
        team VARCHAR(10),
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        PRIMARY KEY (team),
        FOREIGN KEY (team) REFERENCES teamsAll (team)
) Engine = InnoDB;
