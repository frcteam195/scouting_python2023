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
