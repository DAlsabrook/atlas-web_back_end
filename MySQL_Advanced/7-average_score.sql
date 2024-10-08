-- creates a procedure that computes and stores the average score for a student

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    user_id int
)
BEGIN
    DECLARE score_average FLOAT;
    DECLARE passed_id INT = user_id;
    SELECT AVG(score) INTO score_average FROM corrections
    WHERE user_id = passed_id;

    UPDATE users
    SET average_score = score_average
    WHERE id = user_id;
END//
DELIMITER ;
