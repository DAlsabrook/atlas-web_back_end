-- stored procedure
DELIMITER //
CREATE PROCEDURE AddBonus(
    user_id int,
    project_name char(255),
    score int)
BEGIN
    DECLARE project_id INT;

    SELECT id INTO project_id
    FROM projects
    WHERE project.name = project_name;
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END//
DELIMITER ;
