CREATE TABLE IF NOT EXISTS dev1.scouters (
    id INT AUTO_INCREMENT NOT NULL,
    firstName VARCHAR(50) NULL,
    lastName VARCHAR(50) NULL,
    cellPhone VARCHAR(15) NULL, 
    email VARCHAR(100) NULL,
    grade INT NULL,
    PRIMARY KEY (id)
) Engine = InnoDB;
