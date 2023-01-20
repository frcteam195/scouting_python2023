CREATE TABLE IF NOT EXISTS dev1.BAschedule (
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
