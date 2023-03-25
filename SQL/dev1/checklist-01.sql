CREATE TABLE IF NOT EXISTS dev1.checklist
(
    listID    INT AUTO_INCREMENT NOT NULL,
    eventID   INT                NOT NULL,
    matchNum  INT                NOT NULL,
    allianceStationID INT         NULL,
    taskID    INT                NOT NULL,
    scouterID INT                NULL,
    taskStatus INT NULL DEFAULT 0,
    PRIMARY KEY (listID),
    UNIQUE KEY (eventID,matchNum,taskID)
) Engine = InnoDB;