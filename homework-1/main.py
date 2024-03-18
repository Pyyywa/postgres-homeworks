import psycopg2
import os
import csv

#поключение к БД north
connect = psycopg2.connect(
    host = 'localhost',
    database = 'north',
    user = 'postgres',
    password = '0000'
)
try:
    with connect:
        with connect.cursor() as cursor:
            #заполнениe таблицы customers
            with open('north_data/customers_data.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute("INSERT INTO customers (customer_id, company_name, contact_name) "
                                   "VALUES (%s, %s, %s)", row)


            #заполнениe таблицы employees
            with open('north_data/employees_data.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) "
                                   "VALUES (%s, %s, %s, %s, %s, %s)", row)



            #заполнениe таблицы orders
            with open('north_data/orders_data.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) "
                                   "VALUES (%s, %s, %s, %s, %s)", row)


finally:
    connect.close()

