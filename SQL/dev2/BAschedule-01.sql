CREATE TABLE IF NOT EXISTS dev2.BAschedule (
    matchNum INT NOT NULL,
    red1 VARCHAR(10) NOT NULL,
    red2 VARCHAR(10) NOT NULL,
    red3 VARCHAR(10) NOT NULL,
    blue1 VARCHAR(10) NOT NULL,
    blue2 VARCHAR(10) NOT NULL,
    blue3 VARCHAR(10) NOT NULL,
    BAeventID varchar(20) NOT NULL,
    PRIMARY KEY (matchNum),
    FOREIGN KEY (BAeventID) REFERENCES eventsAll (BAeventID)
) Engine = InnoDB;
