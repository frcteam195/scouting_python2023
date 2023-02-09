CREATE TABLE IF NOT EXISTS dev2.dnpList (
        sortOrder INT NOT NULL,
        team VARCHAR(10),
        PRIMARY KEY (sortOrder)
) Engine = InnoDB;