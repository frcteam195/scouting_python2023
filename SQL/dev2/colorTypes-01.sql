CREATE TABLE IF NOT EXISTS dev2.colorTypes (
	colorTypesID INT NOT NULL,
	colorType VARCHAR(50) NULL,
	hex VARCHAR(20) NULL,
	rgb VARCHAR(20) NULL,
	cmyk VARCHAR(20) NULL,
	summary VARCHAR(50) NULL,
	PRIMARY KEY (colorTypesID)
) Engine = InnoDB;
