import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
)
''')


users = [
    ("sanidhya", "sanidhya@example.com"),
    ("shivam", "shivam@example.com"),
    ("lucky", "lucky@example.com")
]

products = [
    ("Laptop", 1200.00),
    ("Smartphone", 800.00),
    ("Headphones", 150.00)
]

orders = [
    (1, 1, 1),
    (2, 2, 2),
    (1, 3, 2)
]

cursor.executemany('INSERT INTO Users (name, email) VALUES (?, ?)', users)
cursor.executemany('INSERT INTO Products (name, price) VALUES (?, ?)', products)
cursor.executemany('INSERT INTO Orders (user_id, product_id, quantity) VALUES (?, ?, ?)', orders)

conn.commit()


print("\nAll Users:")
for row in cursor.execute('SELECT * FROM Users'):
    print(row)

print("\nProducts with price > 500:")
for row in cursor.execute('SELECT * FROM Products WHERE price > 500'):
    print(row)

print("\nJoin Orders with User and Product names:")
query = ('''
SELECT Orders.order_id, Users.name AS user, Products.name AS product, Orders.quantity
FROM Orders
JOIN Users ON Orders.user_id = Users.user_id
JOIN Products ON Orders.product_id = Products.product_id
''')
for row in cursor.execute(query):
    print(row)


cursor.execute("UPDATE Products SET price = price * 0.9 WHERE name = 'Laptop'")
conn.commit()
print("\nUpdated Product Prices:")
for row in cursor.execute('SELECT * FROM Products'):
    print(row)

cursor.execute("DELETE FROM Users WHERE name = 'Charlie'")
conn.commit()
print("\nUsers after deletion:")
for row in cursor.execute('SELECT * FROM Users'):
    print(row)

conn.close()
