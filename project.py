class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []

    def __del__(self):
        pass  # It's not recommended to use __del__ for resource cleanup, consider using context managers

    def list_books(self):
        with open(self.filename, "r") as file:
            for line in file:
                book_name, writer, date, page = line.strip().split(",")
                print(f"Book Name: {book_name}, Writer: {writer}, Release date: {date}, Number of pages: {page}")

    def add_book(self):
        book_name = input("Enter book name: ")
        writer = input("Enter writer: ")
        date = input("Enter release date: ")
        page = input("Enter number of pages: ")

        book_info = f"{book_name},{writer},{date},{page}\n"

        with open(self.filename, "a") as file:
            file.write(book_info)

        print("Book added successfully!")

    def remove_book(self):
        book_name_to_remove = input("Enter book name to remove: ")

        with open(self.filename, "r") as file:
            lines = file.readlines()

        updated_books = [line for line in lines if book_name_to_remove not in line]

        with open(self.filename, "w") as file:
            file.writelines(updated_books)

        print(f"Book '{book_name_to_remove}' removed successfully!")

# Create an object named "lib" with "Library" class
lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")



    

    
    
    