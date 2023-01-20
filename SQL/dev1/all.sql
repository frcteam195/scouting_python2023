CREATE TABLE IF NOT EXISTS dev1.teamsAll (
        team VARCHAR(10),
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        teamCity VARCHAR(50) NULL,
        teamStateProv VARCHAR(50),
        teamCountry VARCHAR(50),
        PRIMARY KEY (team)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.eventsAll (
        BAeventID VARCHAR(20) NOT NULL,
        eventName VARCHAR(100) NOT NULL,
        eventLocation VARCHAR(100) NOT NULL,
        eventStartDate DATE NOT NULL,
        eventEndDate DATE NOT NULL,
        eventWeek INT NOT NULL,
        eventCode VARCHAR(20) NOT NULL,
        PRIMARY KEY (BAeventID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.events (
        id INT UNIQUE,
        BAeventID VARCHAR(20) NOT NULL,
        currentEvent BOOlEAN DEFAULT FALSE,
        eventName VARCHAR(100) NOT NULL,
        eventLocation VARCHAR(100) NOT NULL,
        eventStartDate DATE NOT NULL,
        eventEndDate DATE NOT NULL,
        PRIMARY KEY (BAeventID),
        FOREIGN KEY (BAeventID) REFERENCES eventsAll (BAeventID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.teams (
        team VARCHAR(10),
        BAeventID VARCHAR(20),
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        teamCity VARCHAR(50),
        teamStateProv VARCHAR(50),
        teamCountry VARCHAR(50),
        PRIMARY KEY(team),
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
        FOREIGN KEY (team) REFERENCES teamsAll (team) ON DELETE CASCADE
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.pit (
        team VARCHAR(10),
        BAeventID VARCHAR(20),
        driveType VARCHAR(20),
        PRIMARY KEY(team),
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
        FOREIGN KEY (team) REFERENCES teams (team) ON DELETE CASCADE
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.tmpSchedule (
    MatchNum INT NULL,
    Red1 VARCHAR(10) NULL,
    Red2 VARCHAR(10) NULL,
    Red3 VARCHAR(10) NULL,
    Blue1 VARCHAR(10) NULL,
    Blue2 VARCHAR(10) NULL,
    Blue3 VARCHAR(10) NULL,
    BAeventID VARCHAR(20) NULL,
    PRIMARY KEY (MatchNum),
    FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) 
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.scouters (
    id INT AUTO_INCREMENT NOT NULL,
    firstName VARCHAR(50) NULL,
    lastName VARCHAR(50) NULL,
    cellPhone VARCHAR(15) NULL, 
    email VARCHAR(100) NULL,
    gradYear INT NULL,
    PRIMARY KEY (id)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.matches (
        id INT AUTO_INCREMENT NOT NULL,
        BAeventID VARCHAR(20),
        matchNum INT NOT NULL,
        red1 VARCHAR(10) NOT NULL,
        red2 VARCHAR(10) NOT NULL,
        red3 VARCHAR(10) NOT NULL,
        blue1 VARCHAR(10) NOT NULL,
        blue2 VARCHAR(10) NOT NULL,
        blue3 VARCHAR(10) NOT NULL,
        redAutoPts INT NULL,
        blueAutoPts INT NULL,
        redTelePts INT NULL,
        blueTelePts INT NULL,
        redEndGmPts INT NULL,
        blueEndGmPts INT NULL,
        redScore INT NULL,
        blueScore INT NULL,
        redLinksRP TINYINT NULL,
        blueLinksRP TINYINT NULL,
        redChrgZoneRP TINYINT NULL,
        blueChrgZoneRP TINYINT NULL,
        matchTime INT NULL,
        actualTime INT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.scoutingRole (
        id INT AUTO_INCREMENT NOT NULL,
        scoutingRole VARCHAR(25),
        PRIMARY KEY (id)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.matchScouting (
        id INT AUTO_INCREMENT NOT NULL,
        BAeventID VARCHAR(20) NOT NULL,
        matchID INT NOT NULL,
        matchNum INT NULL,
        scouterID INT NULL,
        scoutingStatus INT NULL,
        team VARCHAR(10) NOT NULL,
        teamMatchNum INT NULL,
        scoutingRoleID INT NULL,
        /* add Level 1 columns here */
        /* add Level 2 columns here. Note that these columns must match those of the level2 DB table */
        PRIMARY KEY (id),
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
        FOREIGN KEY (matchID) REFERENCES matches (id) ON DELETE CASCADE,
        FOREIGN KEY (scouterID) REFERENCES scouters (id) ON DELETE CASCADE,
        FOREIGN KEY (team) REFERENCES teams (team) ON DELETE CASCADE,
        FOREIGN KEY (scoutingRoleID) REFERENCES scoutingRole (id) ON DELETE CASCADE
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.level2 (
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
