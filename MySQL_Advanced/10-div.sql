-- divides the first by the second number

DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN CAST(a as FLOAT) / b;
    END IF;
END//
DELIMITER ;
