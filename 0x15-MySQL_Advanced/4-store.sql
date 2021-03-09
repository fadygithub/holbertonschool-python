-- Trigger the decrease of the quantity of items

CREATE TRIGGER 
reduce_quantity
AFTER INSERT ON orders 
FOR EACH ROW 
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
