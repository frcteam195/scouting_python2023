CREATE TABLE IF NOT EXISTS dev2.analysisTypes (
        analysisTypeID INT NOT NULL,
        analysisType VARCHAR(20),
        runRank BOOLEAN DEFAULT 'FALSE' NOT NULL,
        colorCodeTable BOOLEAN 'FALSE' NOT NULL,
        badMax INT NULL,
        poorMax INT NULL,
        aveMax INT NULL<
        goodMax INT NULL,
        greatMax INT NULL,
        teamPickerOrder INT UNIQUE NULL,
        matchReportOrder INT UNIQUE NULL,
        snapshotOrder INT UNIQUE NULL,
        developer VARCHAR(20) NULL,
        summary VARCHAR(100) NULL,
        PRIMARY KEY (analysisTypeID)
) Engine = InnoDB;
