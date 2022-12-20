from mysql_connector import connection

# ------------------------------- Main Menu Options ---------------------------------

# 1. Insert a publisher
def insertPublisher(name, phone, city):
    cursor = connection.cursor()
    query = "INSERT INTO Publisher (name, phone, city) VALUES (%s, %s, %s)"
    
    # Check of NULL
    if (len(phone) == 0):
        phone = None
    else:
        phone = str(phone)
    if(len(city) == 0):
        city = None

    # Execute Query
    val = (name, phone, city)
    cursor.execute(query, val)
    connection.commit()
    connection.close()

# 2. Insert a book
def insertBook(ISBN, title, year, published_by, previous_edition, price):
    cursor = connection.cursor()
    query = "INSERT INTO Book (ISBN, title, year, published_by, previous_edition, price) VALUES (%s, %s, %s, %s, %s, %s)"

    # Check for NULL
    if(len(title) == 0):
        title = None
    if(len(year) == 0):
        year = None
    else:
        year = str(year)
    if(len(previous_edition) == 0):
        previous_edition = None
    else:
        previous_edition = str(previous_edition)
    if(len(price) == 0):
        price = 0
    else:
        price = str(price)

    # Execute Query
    val = (str(ISBN), title, year, published_by, previous_edition, price)
    cursor.execute(query, val)
    connection.commit()
    connection.close()


# 3. ---------------- Edit Book Options ------------------

# 3. 1. Change ISBN of a Book
def editBookISBN(oldISBN, newISBN):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set ISBN = %s where ISBN = %s"
    val = (str(newISBN), str(oldISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()

# 3. 2. Change Title of a Book
def editBookTitle(ISBN, title):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set title = %s where ISBN = %s"
    val = (title, str(ISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()
    print("done")

# 3. 3. Change Year of a Book
def editBookYear(ISBN, year):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set year = %s where ISBN = %s"
    val = (str(year), str(ISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()

# 3. 4. Change Publisher of a Book
def editBookPublisher(ISBN, publisher):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set published_by = %s where ISBN = %s"
    val = (publisher, str(ISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()

# 3. 5. Change Previous Edition of a Book
def editBookPreviousEdition(ISBN, previous_edition):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set previous_edition = %s where ISBN = %s"
    val = (previous_edition, str(ISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()

# 3. 6. Change Price of a Book
def editBookPrice(ISBN, price):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set price = %s where ISBN = %s"
    val = (str(price), str(ISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()




# 4. ---------------- Delete Book Options ------------------

# 4. 1. Delete book by its ISBN
def deletBookByISBN(ISBN):
    connection.reconnect()
    cursor = connection.cursor()

    # Since there is a foreign key constraint on this query, 
    # we will turn off the checks
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    connection.commit()

    # Executing Query
    query = "DELETE FROM Book WHERE ISBN = %s"
    val = (str(ISBN), )
    cursor.execute(query, val)
    connection.commit()

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")  
    connection.commit()
    connection.close()

# 4. 2. Delete book by its title
def deletBookByTitle(title):
    connection.reconnect()
    cursor = connection.cursor()

    # Since there is a foreign key constraint on this query, 
    # we will turn off the checks
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    connection.commit()

    # Executing Query
    query = "DELETE FROM Book WHERE title = %s"
    val = (title, )
    cursor.execute(query, val)
    connection.commit()

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    connection.commit()
    connection.close()

# 5. ---------------- Search Menu Options ------------------

# 5. 1. Search all books
def findAll():
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"

    # Executing Query
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results
    
# 5. 2. Search books based on title
def findByTitle(title):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title = %s"
    val = (title, )

    # Executing Query
    cursor.execute(query, val)
    results = cursor.fetchall()
    connection.close()
    return results

# 5. 3. Search books based on ISBN
def findByISBN(ISBN):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where ISBN = %s"
    val = (ISBN, )
    
    # Executing Query
    cursor.execute(query, val)
    results = cursor.fetchall()
    connection.close()
    return results

# 5. 4. Search books based on Publisher
def findByPublisher(publisher_name):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where published_by = %s"
    val = (publisher_name, )

    # Executing Query
    cursor.execute(query, val)
    results = cursor.fetchall()
    connection.close()
    return results

# 5. 5. Search books based on a price range
def findByPriceRange(min, max):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where price >= %s and price <= %s"
    val = (min, max)

    # Executing Query
    cursor.execute(query, val)
    results = cursor.fetchall()
    connection.close()
    return results

# 5. 6. Search books based on year
def findByYear(year):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where year = %s"
    val = (year, )

    # Executing Query
    cursor.execute(query, val)
    results = cursor.fetchall()
    connection.close()
    return results

# 5. 7. Search books based on title and publisher
def findByTitlePublisher(title, publisher_name):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title = %s and published_by = %s"
    val = (title, publisher_name)

    # Executing Query
    cursor.execute(query, val)
    results = cursor.fetchall()
    connection.close()
    return results