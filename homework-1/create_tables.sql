CREATE TABLE customers
(
	customer_id varchar(10) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	title varchar(100) NOT NULL,
	birth_date date,
	notes text
);

--вывод таблиц
SELECT * FROM employees

CREATE TABLE orders
(
	order_id char(5) PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date date,
	ship_city varchar(100)
);