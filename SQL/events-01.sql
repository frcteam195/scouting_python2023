CREATE TABLE IF NOT EXISTS dev1.events (
        eventID INT NOT NULL,
        BAeventID VARCHAR(20) NOT NULL,
        currentEvent BOOlEAN DEFAULT FALSE,
        eventName VARCHAR(100) NOT NULL,
        eventLocation VARCHAR(100) NOT NULL,
        eventStartDate DATE NOT NULL,
        eventEndDate DATE NOT NULL,
        timeZone VARCHAR(50) NOT NULL,
        PRIMARY KEY (eventID),
        FOREIGN KEY (BAeventID) REFERENCES eventsAll (BAeventID)
) Engine = InnoDB;
