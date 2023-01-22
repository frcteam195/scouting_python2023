CREATE TABLE IF NOT EXISTS dev1.BAschedule (
    matchNum INT NOT NULL,
    red1 VARCHAR(10) NOT NULL,
    red2 VARCHAR(10) NOT NULL,
    red3 VARCHAR(10) NOT NULL,
    blue1 VARCHAR(10) NOT NULL,
    blue2 VARCHAR(10) NOT NULL,
    blue3 VARCHAR(10) NOT NULL,
    eventID INT NULL,
    PRIMARY KEY (matchNum),
    FOREIGN KEY (eventID) REFERENCES events (id) 
) Engine = InnoDB;
