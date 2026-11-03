with cab as (select customer_id from orders as o1 where product_name='A' and customer_id in (select customer_id from orders as o2 where product_name='B'))

select customer_id, customer_name from customers NATURAL JOIN ((select * from cab) EXCEPT
(select customer_id from orders where product_name='C'
INTERSECT (select * from cab))) order by customer_name