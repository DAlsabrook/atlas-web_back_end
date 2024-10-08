-- creates a procedure that computes and stores the average score for a student

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    user_id int
)
BEGIN
    SELECT AVG(score) AS score_average FROM corrections
    WHERE user_id = user_id;
    UPDATE users
    SET average_score = score_average
    WHERE user_id = user_id;
END//
DELIMITER ;
