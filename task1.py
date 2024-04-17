import requests
import sqlite3


#I have fetched data from external API which has attributes similar to our requirement
response = requests.get("https://my-json-server.typicode.com/dmitrijt9/book-api-mock/books")
books_data = response.json()

#first we connect to sqlite database
conn = sqlite3.connect('mybooks.db')
cursor = conn.cursor()

#create a table to store books with required attributes
cursor.execute("""CREATE TABLE IF NOT EXISTS books
				  (id INTEGER PRIMARY KEY,
				  	author_id INTEGER,
				  	title TEXT,
				  	cover_image TEXT,
				  	pages INTEGER,
				  	releaseDate TEXT,
				  	isbn TEXT)""")


#insert data into our database
for book in books_data:
	cursor.execute("""INSERT INTO books (author_id,title,cover_image,pages,releaseDate,isbn)
					  VALUES(?,?,?,?,?,?)""",(book['author_id'],book['title'],book['cover_image'],book['pages'],book['releaseDate'],book['isbn']))

#to display contents of our database
cursor.execute('''SELECT * FROM books''')
books = cursor.fetchall()
for book in books:
    print(book)


#finally we comit and close our connection
conn.commit()
conn.close()

