CREATE TABLE IF NOT EXISTS dev1.users (
    userID INT AUTO_INCREMENT NOT NULL,
    userName VARCHAR(10) NOT NUll UNIQUE,
    userPass VARCHAR(50) NOT NULL,
    scoutingAccess int NULL,
    analysisAccess int NULL,
    PRIMARY KEY (userID)
) Engine = InnoDB;
