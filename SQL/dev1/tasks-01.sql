CREATE TABLE IF NOT EXISTS dev1.tasks (
    taskID INT NOT NULL,
    task VARCHAR(50) NOT NULL,
    taskDesc TINYTEXT NOT NULL,
    taskStart INT NULL,
    taskFrequency INT NULL,
    taskOrder INT NULL,
    scouterID INT NULL,
    PRIMARY KEY (taskID)
) Engine = InnoDB;