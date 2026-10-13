import requests
import sqlite3


# API URL
api_url = "https://openlibrary.org/search.json"

params = {
    "q": "python",
    "fields": "title,author_name,first_publish_year",
    "limit": 10
}


# 1. Fetch data from API
response = requests.get(api_url, params=params)

if response.status_code == 200:

    data = response.json()

    print("Data fetched successfully!\n")

    books = data["docs"]

else:
    print("Failed to fetch data")
    exit()


# 2. Connect to SQLite
conn = sqlite3.connect("books.db")
cursor = conn.cursor()


# 3. Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publication_year INTEGER
    )
""")


# 4. Store books in database
for book in books:

    title = book.get("title", "Unknown")
    
    authors = book.get("author_name", ["Unknown"])
    author = authors[0]

    publication_year = book.get("first_publish_year", None)

    cursor.execute("""
        INSERT INTO books
        (title, author, publication_year)
        VALUES (?, ?, ?)
    """, (title, author, publication_year))


conn.commit()


# 5. Retrieve data from database
cursor.execute("""
    SELECT * FROM books
""")

stored_books = cursor.fetchall()


# 6. Display books
print("Books stored in SQLite:\n")

for book in stored_books:

    print("ID:", book[0])
    print("Title:", book[1])
    print("Author:", book[2])
    print("Publication Year:", book[3])
    print("-" * 50)


# 7. Close database
conn.close()