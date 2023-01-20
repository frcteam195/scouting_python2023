CREATE TABLE IF NOT EXISTS dev1.analysisTypes (
        id INT NOT NULL,
        analysisType VARCHAR(20),
        teamPickerOrder INT UNIQUE NULL,
        matchReportOrder INT UNIQUE NULL,
        snapshotOrder INT UNIQUE NULL,
        developer VARCHAR(20) NULL,
        summary VARCHAR(100) NULL,
        PRIMARY KEY (id)
) Engine = InnoDB;
