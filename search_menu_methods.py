import book_dao

# Display all the books
def search_all_books():
    results = book_dao.findAll()

    # Display results
    if (results != None):
        print("The following are the ISBNs and titles of all books:")
        for item in results:
            print(item[0], item[1])
        print("The end of books.")
    else:
        print("No Books Exist")

# Display books by their title
def search_by_title():
    # Query Info Input
    title = input("Enter title of the book: ")

    results = book_dao.findByTitle(title)

    # Display results
    if (results != None):
        print("The following are the ISBNs and titles of all books.")
        for item in results:
            print(item[0], item[1])
        print("The end of books.")
    else:
        print("No Books Exist")

# Display books by their ISBN
def search_by_ISBN():
    # Query Info Input
    ISBN = input("Enter ISBN of the book: ")

    results = book_dao.findByISBN(ISBN)

    # Display results
    if (results != None):
        print("The following are the ISBNs and titles of all books.")
        for item in results:
            print(item[0], item[1])
        print("The end of books.")
    else:
        print("No Books Exist")

# Display books by their Publisher
def search_by_publisher():
    # Query Info Input
    publisher_name = input("Enter Publisher of the book: ")

    results = book_dao.findByPublisher(publisher_name)

    # Display results
    if (results != None):
        print("The following are the ISBNs and titles of all books.")
        for item in results:
            print(item[0], item[1])
        print("The end of books.")
    else:
        print("No Books Exist")

# Display books by a price range
def search_by_price_range():
    # Query Info Input
    min = input("Enter minimum Price: ")
    max = input("Enter maximum Price: ")
    
    results = book_dao.findByPriceRange(min, max)

    # Display results
    if (results != None):
        print("The following are the ISBNs and titles of all books.")
        for item in results:
            print(item[0], item[1])
        print("The end of books.")
    else:
        print("No Books Exist")

# Display books by the publication year
def search_by_year():
    # Query Info Input
    year = input("Enter Year of the book: ")

    results = book_dao.findByYear(year)

    # Display results
    if (results != None):
        print("The following are the ISBNs and titles of all books.")
        for item in results:
            print(item[0], item[1])
        print("The end of books.")
    else:
        print("No Books Exist")

# Display books by the title and publisher
def search_by_title_publisher():
    # Query Info Input
    title = input("Enter Title of the book: ")
    publisher_name = input("Enter Publisher name of the book: ")

    results = book_dao.findByTitlePublisher(title, publisher_name)

    # Display results
    if (results != None):
        print("The following are the ISBNs and titles of all books.")
        for item in results:
            print(item[0], item[1])
        print("The end of books.")
    else:
        print("No Books Exist")