CREATE TABLE IF NOT EXISTS dev2.teamsAll (
        team VARCHAR(10),
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        teamCity VARCHAR(50) NULL,
        teamStateProv VARCHAR(50),
        teamCountry VARCHAR(50),
        PRIMARY KEY (team)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.eventsAll (
        BAeventID VARCHAR(20) NOT NULL,
        eventName VARCHAR(100) NOT NULL,
        eventLocation VARCHAR(100) NOT NULL,
        eventStartDate DATE NOT NULL,
        eventEndDate DATE NOT NULL,
        eventWeek INT NOT NULL,
        eventCode VARCHAR(20) NOT NULL,
        PRIMARY KEY (BAeventID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.events (
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
CREATE TABLE IF NOT EXISTS dev2.teams (
        team VARCHAR(10),
        eventID INT,
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        PRIMARY KEY (team, eventID),
        FOREIGN KEY (eventID) REFERENCES events (eventID),
        FOREIGN KEY (team) REFERENCES teamsAll (team)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.BAschedule (
    matchNum INT NOT NULL,
    red1 VARCHAR(10) NOT NULL,
    red2 VARCHAR(10) NOT NULL,
    red3 VARCHAR(10) NOT NULL,
    blue1 VARCHAR(10) NOT NULL,
    blue2 VARCHAR(10) NOT NULL,
    blue3 VARCHAR(10) NOT NULL,
    BAeventID varchar(20) NOT NULL,
    PRIMARY KEY (matchNum),
    FOREIGN KEY (BAeventID) REFERENCES eventsAll (BAeventID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.scouters (
    scouterID INT AUTO_INCREMENT NOT NULL,
    firstName VARCHAR(50) NULL,
    lastName VARCHAR(50) NULL,
    cellPhone VARCHAR(15) NULL, 
    email VARCHAR(100) NULL,
    gradYear INT NULL,
    PRIMARY KEY (scouterID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.matches (
        matchID INT AUTO_INCREMENT NOT NULL,
        eventID INT NOT NULL,
        matchNum INT NOT NULL,
        red1 VARCHAR(10) NOT NULL,
        red2 VARCHAR(10) NOT NULL,
        red3 VARCHAR(10) NOT NULL,
        blue1 VARCHAR(10) NOT NULL,
        blue2 VARCHAR(10) NOT NULL,
        blue3 VARCHAR(10) NOT NULL,
        /* add alliance data from TBA */
        redAutoPts INT NULL,
        blueAutoPts INT NULL,
        redTelePts INT NULL,
        blueTelePts INT NULL,
        redEndGmPts INT NULL,
        blueEndGmPts INT NULL,
        redScore INT NULL,
        blueScore INT NULL,
        redFouls INT NULL,
        blueFouls INT NULL,
        redTechFouls INT NULL,
        blueTechFouls  INT NULL,
        redLinksRP TINYINT NULL,
        blueLinksRP TINYINT NULL,
        redChrgZoneRP TINYINT NULL,
        blueChrgZoneRP TINYINT NULL,
        matchTime VARCHAR(10) NULL,
        actualTime VARCHAR(10) NULL,
        PRIMARY KEY (matchID),
        FOREIGN KEY (eventID) REFERENCES events (eventID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.allianceStations (
        allianceStationID INT AUTO_INCREMENT NOT NULL,
        allianceStation VARCHAR(20),
        PRIMARY KEY (allianceStationID)
) Engine = InnoDB;
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
CREATE TABLE IF NOT EXISTS dev2.BAoprs (
	team VARCHAR(10) NULL,
	OPR FLOAT NULL,
	PRIMARY KEY(team),
	FOREIGN KEY (team) REFERENCES teams (team)
) Engine = InnoDB;CREATE TABLE IF NOT EXISTS dev2.BAranks(
	team VARCHAR(10) NULL,
	rank INT NULL,
	PRIMARY KEY (team),
	FOREIGN KEY (team) REFERENCES teams (team)
) Engine = InnoDB;CREATE TABLE IF NOT EXISTS dev2.colorTypes (
	colorTypesID INT NOT NULL,
	colorType VARCHAR(50) NULL,
	hex VARCHAR(20) NULL,
	rgb VARCHAR(20) NULL,
	cmyk VARCHAR(20) NULL,
	summary VARCHAR(50) NULL,
	PRIMARY KEY (colorTypesID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.BAmatchData (
	matchNum INT NOT NULL,
	eventID INT,
	matchTime VARCHAR(20) NULL,
	actualTime VARCHAR(20) NULL,
	red1 INT NULL,
	red2 INT NULL,
	red3 INT NULL,
	blue1 INT NULL,
	blue2 INT NULL,
	blue3 INT NULL,
	redScore INT NULL,
	blueScore INT NULL,
	/* add additional entries as described in the BA API once it is released for Charged Up */
	PRIMARY KEY (matchNum),
    FOREIGN KEY (eventID) REFERENCES events (eventID)
) Engine = InnoDB;CREATE TABLE IF NOT EXISTS dev2.CEanalysis (
	team VARCHAR(10) NULL,
	analysisTypeID INT NULL,
	eventID INT NULL,
	M1D VARCHAR(10) NULL,
	M1F INT NULL,
	M1V FLOAT NULL,
	M2D VARCHAR(10) NULL,
	M2F INT NULL,
	M2V FLOAT NULL,
	M3D VARCHAR(10) NULL, 
	M3F INT NULL,
	M3V FLOAT NULL,
	M4D VARCHAR(10) NULL, 
	M4F INT NULL,
	M4V FLOAT NULL,
	M5D VARCHAR(10) NULL, 
	M5F INT NULL,
	M5V FLOAT NULL,
	M6D VARCHAR(10) NULL, 
	M6F INT NULL,
	M6V FLOAT NULL,
	M7D VARCHAR(10) NULL, 
	M7F INT NULL,
	M7V FLOAT NULL,
	M8D VARCHAR(10) NULL, 
	M8F INT NULL,
	M8V FLOAT NULL,
	M9D VARCHAR(10) NULL, 
	M9F INT NULL,
	M9V FLOAT NULL,
	M10D VARCHAR(10) NULL, 
	M10F INT NULL,
	M10V FLOAT NULL,
	M11D VARCHAR(10) NULL, 
	M11F INT NULL,
	M11V FLOAT NULL,
	M12D VARCHAR(10) NULL, 
	M12F INT NULL,
	M12V FLOAT NULL,
	S1D VARCHAR(10) NULL, 
	S1F INT NULL,
	S1V FLOAT NULL,
	S2D VARCHAR(10) NULL, 
	S2F INT NULL,
	S2V FLOAT NULL,
	S3D VARCHAR(10) NULL, 
	S3F INT NULL,
	S3V FLOAT NULL,
	S4D VARCHAR(10) NULL, 
	S4F INT NULL,
	S4V FLOAT NULL,
	Min FLOAT NULL,
	Max FLOAT NULL,
	Per FLOAT NULL,
    PRIMARY KEY (team, analysisTypeID, eventID),
    FOREIGN KEY (eventID) REFERENCES events (eventID),
    FOREIGN KEY (team) REFERENCES teams (team),
    FOREIGN KEY (analysisTypeID) REFERENCES analysisTypes (analysisTypeID)
) Engine = InnoDB;CREATE TABLE IF NOT EXISTS dev2.CEanalysisGraphs (
	CEanalysisGraphsID INT NOT NULL,
	team VARCHAR(10) NOT NULL,
	eventID INT NOT NULL,
	teleLowMean FLOAT NULL,
	teleLowMedian FLOAT NULL,
	teleMidMean FLOAT NULL,
	teleMidMedian FLOAT NULL,
	teleHighMean FLOAT NULL,
	teleHighMedian FLOAT NULL,
	teleTotalMean FLOAT NULL,
	teleTotalMedian FLOAT NULL,
	autoRampMean FLOAT NULL,
	autoRampMedian FLOAT NULL,
	autoGamePiecesMean FLOAT NULL,
	autoGamePiecesMedian FLOAT NULL,
	autoScoreMean FLOAT NULL,
	autoScoreMedian FLOAT NULL,
	teleCommunityMean FLOAT NULL,
	teleCommunityMedian FLOAT NULL,
	teleLZPickupMean FLOAT NULL,
	teleLZPickupMedian FLOAT NULL,
	rampMean FLOAT NULL,
	rampMedian FLOAT NULL,
	/* add more once we determine analysisTypes */
    PRIMARY KEY (CEanalysisGraphsID),
    FOREIGN KEY (eventID) REFERENCES events (eventID),
    FOREIGN KEY (team) REFERENCES teams (team)
) Engine = InnoDB;CREATE TABLE IF NOT EXISTS dev2.driveTypes (
        driveTypeID INT NOT NULL,
        driveType VARCHAR(20),
        PRIMARY KEY (driveTypeID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.driveMotorTypes (
        driveMotorTypeID INT NOT NULL,
        driveMotorType VARCHAR(20),
        PRIMARY KEY (driveMotorTypeID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.superClimbTypes (
        superClimbTypeID INT NOT NULL,
        superClimbType VARCHAR(20),
        PRIMARY KEY (superClimbTypeID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.buildTypes (
        buildTypeID INT NOT NULL,
        buildType VARCHAR(20),
        PRIMARY KEY (buildTypeID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.centerGravityTypes (
        centerGravityTypeID INT NOT NULL,
        centerGravityType VARCHAR(20),
        PRIMARY KEY (centerGravityTypeID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.manipulatorTypes (
        manipulatorTypeID INT NOT NULL,
        manipulatorType VARCHAR(20),
        PRIMARY KEY (manipulatorTypeID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.watch1 (
        sortOrder INT NOT NULL,
        team VARCHAR(10),
        PRIMARY KEY (sortOrder)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.watch2 (
        sortOrder INT NOT NULL,
        team VARCHAR(10),
        PRIMARY KEY (sortOrder)
) Engine = InnoDB;CREATE TABLE IF NOT EXISTS dev2.pickList1 (
        sortOrder INT NOT NULL,
        team VARCHAR(10),
        PRIMARY KEY (sortOrder)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.pit (
        team VARCHAR(10) NOT NULL,
        eventID INT NOT NULL,
        scoutingStatus TINYINT DEFAULT 0,
        robotLength TINYINT NULL,
        robotWidth TINYINT NULL,
        robotHeight TINYINT NULL,
        driveBaseTypeID INT NULL,
        driveTypeID INT NULL,
        driveMotorTypeID INT NULL,
        manipulatorTypeID INT NULL,
        dedicatedGroundIntake TINYINT NULL,
        superClimbTypeID INT NULL,
        buildTypeID INT NULL,
        centerGravityTypeID INT NULL,
        robotDurability TINYINT NULL,
        buildQuality TINYINT NULL,
        buildComments TINYTEXT NULL,
        electricalQuality TINYINT NULL,
        electricalComments TINYTEXT NULL,
        generalComments TINYTEXT NULL,
        imageLink VARCHAR(150) NULL,
        PRIMARY KEY (team),
        FOREIGN KEY (team) REFERENCES teams (team),
        FOREIGN KEY (eventID) REFERENCES events (eventID),
        FOREIGN KEY (manipulatorTypeID) REFERENCES manipulatorTypes (manipulatorTypeID),
        FOREIGN KEY (driveMotorTypeID) REFERENCES driveMotorTypes (driveMotorTypeID),
        FOREIGN KEY (superClimbTypeID) REFERENCES superClimbTypes (superClimbTypeID),
        FOREIGN KEY (buildTypeID) REFERENCES buildTypes (buildTypeID),
        FOREIGN KEY (driveTypeID) REFERENCES driveTypes (driveTypeID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.matchScouting (
        matchScoutingID INT AUTO_INCREMENT NOT NULL,
        eventID INT NOT NULL,
        matchID INT NOT NULL,
        matchNum INT NULL,
        allianceStationID INT NULL,
        team VARCHAR(10) NOT NULL,
        teamMatchNum INT NULL,
        scoutingStatus INT NULL,
        scouterID INT NULL,
        /* Level 1 Data */
        preStartPos TINYINT NULL,
        preLoad TINYINT NULL,
        preNoShow TINYINT NULL,
        autoMB TINYINT NULL,
        autoRamp TINYINT NULL,
        autoPen TINYINT NULL,
        autoGamePiece1 TINYINT NULL,
        autoGamePiece2 TINYINT NULL,
        autoGamePiece3 TINYINT NULL,
        autoGamePiece4 TINYINT NULL,
        autoScore1 TINYINT NULL,
        autoScore2 TINYINT NULL,
        autoScore3 TINYINT NULL,
        autoScore4 TINYINT NULL,
        teleConeHigh TINYINT NULL,
        teleCubeHigh TINYINT NULL,
        teleConeMid TINYINT NULL,
        teleCubeMid TINYINT NULL,
        teleConeLow TINYINT NULL,
        teleCubeLow TINYINT NULL,
        teleConeCMTY TINYINT NULL,
        teleCubeCMTY TINYINT NULL,
        teleLZPickup TINYINT NULL,
        teleObstructed TINYINT NULL,
        teleWasObstructed TINYINT NULL,
        ramp TINYINT NULL,
        rampAssist TINYINT NULL,
        rampPos TINYINT NULL,
        rampStartTime TINYINT NULL,
        postSubsystemBroke TINYINT NULL,
        postBrokeDown TINYINT NULL,
        postReorientCone TINYINT NULL,
        postShelfPickup TINYINT NULL,
        postGroundPickup TINYINT NULL,
        postGoodPartner TINYINT NULL,
        PRIMARY KEY (matchScoutingID),
        FOREIGN KEY (eventID) REFERENCES events (eventID),
        FOREIGN KEY (matchID) REFERENCES matches (matchID),
        FOREIGN KEY (scouterID) REFERENCES scouters (scouterID),
        FOREIGN KEY (team) REFERENCES teams (team),
        FOREIGN KEY (allianceStationID) REFERENCES allianceStations (allianceStationID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.matchScoutingL2 (
        matchScoutingL2ID INT AUTO_INCREMENT NOT NULL,
        eventID INT NOT NULL,
        matchID INT NOT NULL,
        matchNum INT NULL,
        allianceStationID INT NULL,
        team VARCHAR(10) NOT NULL,
        teamMatchNum INT NULL,
        scoutingStatus INT NULL,
        scouterID INT NULL,
        synced2MS BOOLEAN DEFAULT false,
        /* add Level 2 columns here. Note that these columns must match those of the matchScouting DB table */
        speed TINYINT NULL,
        maneuverability TINYINT NULL,
        sturdiness TINYINT NULL,
        climb TINYINT NULL,
        effort TINYINT NULL,
        scoringEff TINYINT NULL,
        intakeEff TINYINT NULL,
        commentOff TINYTEXT NULL,
        commentDef TINYTEXT NULL,
        goodOffBot TINYINT NULL,
        goodDefBot TINYINT NULL,
        defCommunity TINYINT NULL,
        defCenter TINYINT NULL,
        defLZ TINYINT NULL,        
        PRIMARY KEY (matchScoutingL2ID),
        FOREIGN KEY (eventID) REFERENCES events (eventID),
        FOREIGN KEY (matchID) REFERENCES matches (matchID),
        FOREIGN KEY (scouterID) REFERENCES scouters (scouterID),
        FOREIGN KEY (team) REFERENCES teams (team),
        FOREIGN KEY (allianceStationID) REFERENCES allianceStations (allianceStationID)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.BAteams (
        team VARCHAR(10),
        teamName VARCHAR(50),
        teamLocation VARCHAR(50),
        PRIMARY KEY (team),
        FOREIGN KEY (team) REFERENCES teamsAll (team)
) Engine = InnoDB;
CREATE TABLE IF NOT EXISTS dev2.dnpList (
        sortOrder INT NOT NULL,
        team VARCHAR(10),
        PRIMARY KEY (sortOrder)
) Engine = InnoDB;CREATE TABLE IF NOT EXISTS dev2.final24 (
        sortOrder INT NOT NULL,
        team VARCHAR(10),
        PRIMARY KEY (sortOrder)
) Engine = InnoDB;