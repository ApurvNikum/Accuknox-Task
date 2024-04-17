-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Create products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2)
);

-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create order details table
CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10, 2),
    total_price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data into customers table
INSERT INTO customers (customer_id, name, email) VALUES
(1, 'Apurv Nikum', 'apurvnikum@gmail.com'),
(2, 'Praveen Kumar', 'praveenk@gmail.com');

-- Insert sample data into products table
INSERT INTO products (product_id, name, price) VALUES
(1, 'Smartwatch', 1000),
(2, 'Speakers', 850);

-- Insert sample data into orders table
INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES
(1, 1, '2023-02-17', 1800),
(2, 2, '2023-02-18', 800);

-- Insert sample data into order details table
INSERT INTO order_details (order_detail_id, order_id, product_id, quantity, unit_price, total_price) VALUES
(1, 1, 1, 1, 1000, 1000),
(2, 1, 2, 1, 800, 800),
(3, 2, 2, 1, 800, 800);

-- Create trigger to update total amount in orders table after inserting order details
CREATE TRIGGER update_total_amount
AFTER INSERT ON order_details
BEGIN
    UPDATE orders
    SET total_amount = (
        SELECT SUM(total_price)
        FROM order_details
        WHERE order_id = NEW.order_id
    )
    WHERE order_id = NEW.order_id;
END;

-- Common table expression (CTE) to fetch order details with product names
WITH OrderDetailsWithProductNames AS (
    SELECT od.order_id, p.name AS product_name, od.quantity, od.unit_price, od.total_price
    FROM order_details od
    JOIN products p ON od.product_id = p.product_id
)
-- Query to fetch order details along with product names and customer names
SELECT o.order_id, c.name AS customer_name, od.product_name, od.quantity, od.unit_price, od.total_price
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN OrderDetailsWithProductNames od ON o.order_id = od.order_id;
