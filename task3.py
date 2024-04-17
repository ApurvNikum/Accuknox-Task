import csv
import sqlite3

# Read data from CSV file
with open('users.csv', 'r') as file:
    csv_reader = csv.reader(file)
    data = list(csv_reader)

# Connect to SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a table to store users if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY,
                  Name TEXT,
                  email TEXT)''')

# Insert data from CSV into the database
for row in data:
    cursor.execute('''INSERT INTO users (name, email)
                      VALUES (?, ?)''', (row[0], row[1]))


cursor.execute('''SELECT * FROM users''')
users = cursor.fetchall()
for user in users:
    print(user)
    
# Commit changes and close connection
conn.commit()
conn.close()
