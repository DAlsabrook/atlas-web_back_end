-- divides the first by the second number

DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    IF b = 0
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END//
DELIMITER ;
