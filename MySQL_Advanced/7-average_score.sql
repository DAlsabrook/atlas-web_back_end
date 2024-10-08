-- creates a procedure that computes and stores the average score for a student

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id int
)
BEGIN
    DECLARE score_average FLOAT;

    SELECT AVG(score) INTO score_average FROM corrections
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = score_average
    WHERE id = user_id;
END//
DELIMITER ;
