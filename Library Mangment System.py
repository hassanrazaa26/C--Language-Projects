class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, copies):
        if title in self.books:
            self.books[title] += copies
        else:
            self.books[title] = copies
        print(f"Added {copies} copies of '{title}' to the library.")

    def display_books(self):
        print("\nLibrary Book List:")
        print("{:<30} {:<10}".format("Title", "Available Copies"))
        print("-" * 45)
        for title, copies in self.books.items():
            print("{:<30} {:<10}".format(title, copies))
        print("-" * 45)

    def borrow_book(self, title, num_copies):
        if title in self.books and self.books[title] >= num_copies:
            self.books[title] -= num_copies
            print(f"You have borrowed {num_copies} copies of '{title}'.")
        else:
            print(f"Sorry, '{title}' is either not available or insufficient copies.")

    def return_book(self, title, num_copies):
        if title in self.books:
            self.books[title] += num_copies
            print(f"You have returned {num_copies} copies of '{title}'.")
        else:
            print(f"Invalid return. '{title}' is not in the library.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            copies = int(input("Enter the number of copies: "))
            library.add_book(title, copies)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter the title of the book you want to borrow: ")
            copies = int(input("Enter the number of copies you want to borrow: "))
            library.borrow_book(title, copies)

        elif choice == '4':
            title = input("Enter the title of the book you want to return: ")
            copies = int(input("Enter the number of copies you want to return: "))
            library.return_book(title, copies)

        elif choice == '5':
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
