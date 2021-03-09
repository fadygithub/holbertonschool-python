-- Reset the attribute valid_email with a trigger when email is modified

DELIMITER $$
CREATE TRIGGER 
validate_email
BEFORE UPDATE 
ON users FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
    SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;
