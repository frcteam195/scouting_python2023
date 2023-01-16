CREATE TABLE IF NOT EXISTS dev1.teams (
        team VARCHAR(10),
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        teamCity VARCHAR(50) NULL,
        teamStateProv VARCHAR(50),
        teamCountry VARCHAR(50),
        PRIMARY KEY (team)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.allEvents (
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
        FOREIGN KEY (BAeventID) REFERENCES allEvents (BAeventID)
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
CREATE TABLE IF NOT EXISTS dev1.CEteams (
        team VARCHAR(10),
        BAeventID VARCHAR(20),
        driveType VARCHAR(20),
        PRIMARY KEY(team),
        FOREIGN KEY (BAeventID) REFERENCES events (BAeventID) ON DELETE CASCADE,
        FOREIGN KEY (team) REFERENCES BAteams (team) ON DELETE CASCADE
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev1.tmpSchedule (
    MatchNum INT NULL,
    Red1 VARCHAR(10) NULL,
    Red2 VARCHAR(10) NULL,
    Red3 VARCHAR(10) NULL,
    Blue1 VARCHAR(10) NULL,
    Blue2 VARCHAR(10) NULL,
    Blue3 VARCHAR(10) NULL,
    BAEventsID VARCHAR(20) NULL,
    PRIMARY KEY (MatchNum)
) Engine = InnoDB;
