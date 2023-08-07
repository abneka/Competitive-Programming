# Write your MySQL query statement below
select d.name as "Department", e.name as "Employee", e.salary as "Salary"
from Employee e
inner join (
    select departmentId, max(salary) as max_salary from Employee
    group by departmentId
) 
max_salaries 
on e.salary = max_salaries.max_salary
and e.departmentId = max_salaries.departmentId
join Department d on d.id = e.departmentId;