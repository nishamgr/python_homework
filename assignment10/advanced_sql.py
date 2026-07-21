import sqlite3
import pandas as pd

#connecting to the db
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")


#TaskTask 1: Complex JOINs with Aggregation
1
query1 = """
SELECT 
    o.order_id,
    SUM(p.price * li.quantity) AS total_price
FROM orders o 
JOIN line_items li
    ON o.order_id = li.order_id
JOIN products p
    ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;

"""

#Task 2: Understanding Subqueries

query2 = """
SELECT
    c.customer_name,
    AVG(sub.total_price) AS average_total_price
FROM customers c 
LEFT JOIN(
    SELECT
        o.customer_id AS customer_id_b,
        SUM(p.price * li.quantity) AS total_price
    FROM orders o 
    JOIN line_items li
        ON o.order_id = li.order_id
    JOIN products p
        ON li.product_id = p.product_id
    GROUP BY o.order_id, o.customer_id
) sub
ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id
LIMIT 5;

"""
#Task 3: An Insert Transaction Based on Data
conn.execute("PRAGMA foregin_keys = 1")
cursor = conn.cursor()

customer_id = 16
employee_id = 7

cursor.execute("""
INSERT INTO orders (
    customer_id,
    employee_id
)
VALUES(?,?)
RETURNING order_id
""", (customer_id, employee_id))
       
order_id = cursor.fetchone()[0]

products = [23, 18, 43, 9, 44]

for product_id in products:
    cursor.execute("""
    INSERT INTO line_items (
        order_id,
        product_id,
        quantity
    )
    VALUES(?,?,?)
    """, (order_id, product_id, 10))

conn.commit()

query3 = """
SELECT 
    li.line_item_id,
    li.quantity,
    p.product_name
FROM line_items li
JOIN products p
        ON li.product_id = p.product_id
WHERE li.order_id = ?
"""


#query and store result in df
df1 = pd.read_sql_query(query1, conn)
print("Task 1, Total price of first 5 orders:")
print(df1)

print()

df2 = pd.read_sql_query(query2, conn)
print("Task 2, Avg order price by customer:")
print(df2)

df3 = pd.read_sql_query(query3, conn, params=(order_id,))
print("Task3, New Order:")
print(df3)

#Task 4: Aggregation with HAVING
query4 = """
SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    COUNT(o.order_id) AS order_count
FROM employees e
JOIN orders o
    ON e.employee_id = o.employee_id
GROUP BY
    e.employee_id,
    e.first_name,
    e.last_name
HAVING COUNT(o.order_id) > 5;
"""
df4 = pd.read_sql_query(query4, conn)
print("Task 4, Employees with more than 5 orders")
print(df4)
#close conn
conn.close()