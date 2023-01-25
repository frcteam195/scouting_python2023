CREATE TABLE IF NOT EXISTS dev2.analysisTypes (
        analysisTypeID INT NOT NULL,
        analysisType VARCHAR(20),
        teamPickerOrder INT UNIQUE NULL,
        matchReportOrder INT UNIQUE NULL,
        snapshotOrder INT UNIQUE NULL,
        developer VARCHAR(20) NULL,
        summary VARCHAR(100) NULL,
        PRIMARY KEY (analysisTypeID)
) Engine = InnoDB;
