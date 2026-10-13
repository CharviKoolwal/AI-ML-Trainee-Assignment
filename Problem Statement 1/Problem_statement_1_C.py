import csv
import sqlite3


# Step 1: Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()


# Step 2: Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")


# Step 3: Read data from CSV file
with open("users.csv", "r") as file:

    csv_reader = csv.DictReader(file)

    for row in csv_reader:

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (row["name"], row["email"])
        )


# Step 4: Save changes
conn.commit()


# Step 5: Display data from database
cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

for user in users:
    print(user)


# Step 6: Close database connection
conn.close()