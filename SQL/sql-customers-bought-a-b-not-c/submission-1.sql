-- Write your query below
SELECT DISTINCT c.customer_id, c.customer_name 
FROM customers c
WHERE c.customer_id IN (SELECT customer_id from orders WHERE product_name = 'A')
AND c.customer_id in (SELECT customer_id from orders WHERE product_name = 'B')
AND NOT c.customer_id in (SELECT customer_id from orders WHERE product_name = 'C')
ORDER BY  customer_name;