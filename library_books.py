library_books = []

# ---- ADD BOOK ----
def add_books():
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "name": name,
        "author": author
    }

    library_books.append(book)
    print("Book Added Successfully!")


# ---- SHOW BOOKS ----
def show_books():
    if not library_books:
        print("No Books Available")
    else:
        print("\nAvailable Books:")
        for book in library_books:
            print(f"{book['name']} | Author: {book['author']}")


# ---- ISSUE BOOK ----
def issue_books():
    show_books()
    name = input("Enter Book Name to Issue: ")

    for book in library_books:
        if book["name"] == name:
            library_books.remove(book)
            print("Book Issued Successfully!")
            return

    print("Book not available")


# ---- RETURN BOOK ----
def return_books():
    name = input("Enter Book Name to Return: ")
    author = input("Enter Author Name: ")

    book = {
        "name": name,
        "author": author
    }

    library_books.append(book)
    print("Book Returned Successfully!")


# ---- MAIN ----
def library():
    while True:
        print("\n1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_books()
        elif choice == "2":
            show_books()
        elif choice == "3":
            issue_books()
        elif choice == "4":
            return_books()
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print("Invalid Choice")


library()