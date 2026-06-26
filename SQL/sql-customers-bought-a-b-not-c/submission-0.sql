-- Write your query below
SELECT DISTINCT c.customer_id, c.customer_name 
FROM customers c JOIN orders o ON c.customer_id = o.customer_id
WHERE o.customer_id IN (SELECT customer_id from orders WHERE product_name = 'A')
AND o.customer_id in (SELECT customer_id from orders WHERE product_name = 'B')
AND NOT o.customer_id in (SELECT customer_id from orders WHERE product_name = 'C')
ORDER BY  customer_name;