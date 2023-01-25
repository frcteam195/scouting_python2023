CREATE TABLE IF NOT EXISTS dev2.scouters (
    scouterID INT AUTO_INCREMENT NOT NULL,
    firstName VARCHAR(50) NULL,
    lastName VARCHAR(50) NULL,
    cellPhone VARCHAR(15) NULL, 
    email VARCHAR(100) NULL,
    gradYear INT NULL,
    PRIMARY KEY (scouterID)
) Engine = InnoDB;
