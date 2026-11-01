-- Write your query below
select employee_id, case when (employee_id%2)=1 and name NOT LIKE 'M%' THEN salary ELSE 0 END as bonus from employees order by employee_id;