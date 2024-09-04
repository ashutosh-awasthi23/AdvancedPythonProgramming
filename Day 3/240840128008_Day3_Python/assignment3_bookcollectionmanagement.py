def display_menu():
    print("\nBook Collection Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Exit")


def add_book(collection):
    title = input("Enter the book title: ")
    if title in collection:
        print("This book already exists in the collection.")
    else:
        author = input("Enter the author's name: ")
        genre = input("Enter the genre: ")
        year = input("Enter the year of publication: ")
        collection[title] = {
            'author': author,
            'genre': genre,
            'year': year
        }
        print(f"Book '{title}' added successfully.")


def remove_book(collection):
    title = input("Enter the book title to remove: ")
    if title in collection:
        del collection[title]
        print(f"Book '{title}' removed successfully.")
    else:
        print("This book is not in the collection.")


# def search_book(collection):
#     title = input("Enter the book title to search: ")
#     if title in collection:
#         book = collection[title]
#         print(f"\nTitle: {title}")
#         print(f"Author: {book['author']}")
#         print(f"Genre: {book['genre']}")
#         print(f"Year: {book['year']}")
#     else:
#         print("This book is not in the collection.")

def search_book(collection):
    print("\nSearch by:")
    print("1. Title")
    print("2. Author")
    print("3. Genre")

    search_choice = input("Enter your choice (1-3): ")

    if search_choice == '1':
        title = input("Enter the book title to search: ")
        if title in collection:
            book = collection[title]
            print(f"\nTitle: {title}")
            print(f"Author: {book['author']}")
            print(f"Genre: {book['genre']}")
            print(f"Year: {book['year']}")
        else:
            print("This book is not in the collection.")

    elif search_choice == '2':
        author = input("Enter the author's name to search: ")
        found = False
        for title, details in collection.items():
            if details['author'].lower() == author.lower():
                print(f"\nTitle: {title}")
                print(f"Author: {details['author']}")
                print(f"Genre: {details['genre']}")
                print(f"Year: {details['year']}")
                found = True
        if not found:
            print("No books found for this author.")

    elif search_choice == '3':
        genre = input("Enter the genre to search: ")
        found = False
        for title, details in collection.items():
            if details['genre'].lower() == genre.lower():
                print(f"\nTitle: {title}")
                print(f"Author: {details['author']}")
                print(f"Genre: {details['genre']}")
                print(f"Year: {details['year']}")
                found = True
        if not found:
            print("No books found for this genre.")

    else:
        print("Invalid choice. Please choose a number between 1 and 3.")


def display_books(collection):
    if not collection:
        print("No books in the collection.")
    else:
        for title, details in collection.items():
            print(f"\nTitle: {title}")
            print(f"Author: {details['author']}")
            print(f"Genre: {details['genre']}")
            print(f"Year: {details['year']}")


def main():
    book_collection = {}

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_book(book_collection)
        elif choice == '2':
            remove_book(book_collection)
        elif choice == '3':
            search_book(book_collection)
        elif choice == '4':
            display_books(book_collection)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()
