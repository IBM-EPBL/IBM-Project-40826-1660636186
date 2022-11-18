import sqlite3

conn = sqlite3.connect('customer.db')
print("Opened database successfully")

conn.execute('CREATE TABLE customer(name TEXT, address TEXT, city TEXT, phonenumber TEXT)')
print("Table created successfully")
conn.close()