-- creates a procedure that computes and stores the average score for a student

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    user_id int
)
BEGIN
    DECLARE score_average DECIMAL(10, 2);

    SELECT AVG(score) INTO score_average FROM corrections
    WHERE user_id = user_id;

    UPDATE users
    SET average_score = score_average
    WHERE id = user_id;
END//
DELIMITER ;
