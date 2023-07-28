CREATE DATABASE IF NOT EXISTS products;
USE products;
CREATE TABLE IF NOT EXISTS items_on_sale (
   name VARCHAR(24),
   qty INT(4),
   price DECIMAL(10, 2)
);
INSERT INTO items_on_sale (name, qty, price)
VALUES ('Muffins', 4, 2.99),
   ('Cake', 20, 12.50),
   ('Nails', 100, 0.50),
   ('Coke', 25, 7.0),
   ('Kitkat', 100, 3.0),
   ('Shake', 100, 2.50);
-- Add more INSERT INTO statements for additional products if needed