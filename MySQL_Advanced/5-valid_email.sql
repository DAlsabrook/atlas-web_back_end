-- creates a trigger that resets valid_email when the email has been changed

delimiter //
CREATE TRIGGER update_valid_email AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    ELSE
        SET NEW.valid_email = 1;
    END IF;
END//
delimiter ;
