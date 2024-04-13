import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (name TEXT, email TEXT, gender TEXT)''')

# Read the CSV file and insert the data into the database
with open('D:/div/ML/API/API/Storing CSV to SQLite/dataset.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['first_name']
        email = row['email']
        gender = row['gender']
        c.execute("INSERT INTO users (name, email, gender) VALUES (?, ?, ?)", (name, email, gender))

# Commit the changes and close the connection
conn.commit()

res = c.execute("SELECT * FROM users")
entry = res.fetchall()
print(entry)

conn.close()