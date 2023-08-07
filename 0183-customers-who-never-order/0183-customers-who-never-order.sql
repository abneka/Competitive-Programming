# Write your MySQL query statement below
# select name as Customers from Customers where id not in (select customerId from Orders);
select name as Customers from Customers 
left join Orders on Customers.id = Orders.customerId 
where Orders.customerId is NULL;