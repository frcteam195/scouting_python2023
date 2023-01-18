CREATE TABLE IF NOT EXISTS dev1.teams (
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
        id INT AUTO_INCREMENT NOT NULL,
        BAeventID VARCHAR(20) NULL,
        currentEvent BOOlEAN DEFAULT FALSE,
        eventName VARCHAR(100) NULL,
        eventLocation VARCHAR(100) NULL,
        eventStartDate DATE NULL,
        eventEndDate DATE NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (BAeventID) REFERENCES eventsAll (BAeventID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.CEteams (
        team VARCHAR(10),
        BAeventID VARCHAR(20),
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        teamCity VARCHAR(50),
        teamStateProv VARCHAR(50),
        teamCountry VARCHAR(50),
        PRIMARY KEY(team),
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
        FOREIGN KEY (team) REFERENCES teams (team) ON DELETE CASCADE
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
    grade INT NULL,
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
        FOREIGN KEY (matchID) REFERENCES matches (id) ON DELETE CASCADE,
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE
) Engine = InnoDB;
