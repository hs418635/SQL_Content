use db_design;
show tables;
describe customer;

-- Inserting records into Customer table
INSERT INTO Customer (customer_id, name, email, address)
VALUES 
    (1, 'Aarav Patel', 'aarav@example.com', '123, ABC Street, Mumbai'),
    (2, 'Ishaan Singh', 'ishaan@example.com', '456, XYZ Road, Delhi'),
    (3, 'Avani Sharma', 'avani@example.com', '789, PQR Avenue, Bangalore'),
    (4, 'Anaya Gupta', 'anaya@example.com', '1011, LMN Lane, Kolkata'),
    (5, 'Riya Joshi', 'riya@example.com', '1213, EFG Avenue, Chennai');
    
select * from customer;

-- Inserting records into Order table
-- Assume customer_id starts from 1 and increments for each new customer
INSERT INTO Orders(order_id, customer_id, order_date)
VALUES 
    (1, 1, '2024-04-12'),
    (2, 2, '2024-04-12'),
    (3, 3, '2024-04-13'),
    (4, 4, '2024-04-13'),
    (5, 5, '2024-04-14');
select * from orders;

-- Inserting records into Payment table
-- Assume payment_id starts from 1 and increments for each new payment
INSERT INTO Payment (payment_id, order_id, amount, payment_date)
VALUES 
    (1, 1, 1500.00, '2024-04-12'),
    (2, 2, 800.00, '2024-04-12'),
    (3, 3, 3000.00, '2024-04-13'),
    (4, 4, 2500.00, '2024-04-13'),
    (5, 5, 1200.00, '2024-04-14');
select * from payment;

-- Inserting records into Product table
INSERT INTO Product (product_id, name, price, inventory)
VALUES 
    (1, 'Saree', 1500.00, 50),
    (2, 'Kurta', 800.00, 30),
    (3, 'Lehenga', 3000.00, 20),
    (4, 'Sherwani', 2500.00, 25),
    (5, 'Salwar Suit', 1200.00, 40);
    
select * from product;
