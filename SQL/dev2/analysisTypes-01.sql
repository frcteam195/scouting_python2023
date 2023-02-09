CREATE TABLE IF NOT EXISTS dev2.analysisTypes (
        analysisTypeID INT NOT NULL,
        analysisType VARCHAR(20),
        runRank BOOLEAN DEFAULT 0 NOT NULL,
        colorCodeTable BOOLEAN DEFAULT 0 NOT NULL,
        badMax INT NULL,
        poorMax INT NULL,
        aveMax INT NULL,
        goodMax INT NULL,
        greatMax INT NULL,
        teamPicker INT NULL,
        matchReport INT NULL,
        sortOrder INT NULL,
        robotSnapshot INT NULL,
        developer VARCHAR(20) NULL,
        summary VARCHAR(100) NULL,
        PRIMARY KEY (analysisTypeID)
) Engine = InnoDB;
