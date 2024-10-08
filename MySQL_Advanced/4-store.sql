-- creates a trigger that decreases the quantity of an item after new order.

delimiter //
CREATE TRIGGER update_quantity AFTER INSERT ON orders
FOR EACH ROW
    BEGIN
        UPDATE items
        SET items.quantity = items.quantity - NEW.number
        WHERE items.name = NEW.item_name;
    END//
delimiter ;
