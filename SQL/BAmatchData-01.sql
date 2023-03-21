CREATE TABLE IF NOT EXISTS dev1.BAmatchData (
	matchNum INT NOT NULL,
	eventID INT,
	matchTime VARCHAR(20) NULL,
	actualTime VARCHAR(20) NULL,
	/* teams */
	red1 INT NULL,
	red2 INT NULL,
	red3 INT NULL,
	blue1 INT NULL,
	blue2 INT NULL,
	blue3 INT NULL,
	/* total counts */
	redTotalCSPts INT NULL,
	blueTotalCSPts INT NULL,
	redTotalPts INT NULL,
	blueTotalPts INT NULL,
	redLinkPts INT NULL,
	blueLinkPts INT NULL,
	redCoopGamePieceCount INT NULL,
	blueCoopGamePieceCount INT NULL,
	/* Bonuses */
    redActivationBonus INT NULL,
	blueActivationBonus INT NULL,
	redCoopertitionBonus INT NULL,
	blueCoopertitionBonus INT NULL,
	redSustainabilityBonus INT NULL,
    blueSustainabilityBonus INT NULL,
	/* fouls */
	redFouls INT NULL,
	blueFouls INT NULL,
	redTechFouls INT NULL,
	blueTechFouls INT NULL,
	/* autoautonomous */
	redAutoMoveBonusPts INT NULL,
	blueAutoMoveBonusPts INT NULL,
	redAutoGamePieces INT NULL,
	blueAutoGamePieces INT NULL,
	redAutoGamePiecePts INT NULL,
	blueAutoGamePiecePts INT NULL,
	redAutoCSPts INT NULL,
	blueAutoCSPts INT NULL,
	redAutoPts INT NULL,
	blueAutoPts INT NULL,
    /* teleop */
	redTeleGamePieces INT NULL,
	blueTeleGamePieces INT NULL,
	redTeleGamePiecePts INT NULL,
	blueTeleGamePiecePts INT NULL,
	redTelePts INT NULL,
	blueTelePts INT NULL,
	/* endgame */
	redEndgameCSPts INT NULL,
	blueEndgameCSPts INT NULL,
	PRIMARY KEY (matchNum),
    FOREIGN KEY (eventID) REFERENCES events (eventID)
) Engine = InnoDB;