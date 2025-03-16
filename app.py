# libaray management system

# step 1
# make an empty list 
library_store = []

# Step 2: Add a book
def addBook():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    typeOfBook = input("Enter the genre: ")
    ifRead = input("Have you read this book? (yes/no): ")
    book = {"title": title, "author": author, "year": year, "typeOfBook": typeOfBook, "ifRead": ifRead}
    library_store.append(book)
    print("------------------------------")
    print(f"Book '{title}' added successfully!")

# Step 3: Remove a book
def removeBook():
    titleRemove = input("Enter the title of the book to remove: ")
    for book in library_store:
        if book["title"].lower() == titleRemove.lower():
            library_store.remove(book)
            print("------------------------------")
            print(f"Book '{titleRemove}' has been removed!")
            return
    print("------------------------------")
    print(f"Book '{titleRemove}' is not found in the library.")

# Step 4: Search for a book
def searchBook():
    print("\n🔍 Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        title = input("Enter the title: ")
        found = False
        for book in library_store:
            if book["title"].lower() == title.lower():
                print(f"Matching Book:")
                print(f"{book['title']} by {book['author']} ({book['year']}) - {book['typeOfBook']} - Read: {book['ifRead']}")
                found = True
                break
        if not found:
            print(f"No book found with title '{title}'.")

    elif choice == "2":
        author = input("Enter the author: ")
        found_books = [book for book in library_store if book["author"].lower() == author.lower()]
        if found_books:
            print(f"Books by {author}:")
            for book in found_books:
                print(f"{book['title']} ({book['year']}) - {book['typeOfBook']} - Read: {book['ifRead']}")
        else:
            print(f"No books found by author '{author}'.")

    else:
        print("Invalid choice. Please try again.")

# Step 5: Display all books
def displayBook():
    if not library_store:
        print("The library is empty.")
    else:
        print("Your library:")
        for book in library_store:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['typeOfBook']} - Read: {book['ifRead']}")

# Step 6: Display statistics
def displayStatistic():
    if not library_store:
        print("The library is empty.")
    else:
        totalBooks = len(library_store)
        authors = [book["author"] for book in library_store]
        uniqueAuthors = len(set(authors))
        print(f"Total books: {totalBooks}")
        print(f"Unique authors: {uniqueAuthors}")

# Step 7: Save library to a file
def saveLibraryToFile():
    with open("library.txt", "w") as file:
        for book in library_store:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['typeOfBook']},{book['ifRead']}\n")
    print(f"Library saved to {file.name}")
def main():
    while True:
        print("------------------------------")
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        print("------------------------------")
        choice = input("Enter your choice: ")

        if choice == "1":
            addBook()
        elif choice == "2":
            removeBook()
        elif choice == "3":
            searchBook()
        elif choice == "4":
            displayBook()
        elif choice == "5":
            displayStatistic()
        elif choice == "6":
            saveLibraryToFile()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Running the program
if __name__ == "__main__":
    main()