-- Write your query below
select name from customers where id not in (select customers.id from customers, orders where customers.id=orders.customer_id)