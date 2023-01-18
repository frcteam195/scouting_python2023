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
