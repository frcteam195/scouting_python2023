CREATE TABLE IF NOT EXISTS dev1.buildTypes (
        buildTypeID INT NOT NULL,
        buildType VARCHAR(20),
        PRIMARY KEY (buildTypeID)
) Engine = InnoDB;
