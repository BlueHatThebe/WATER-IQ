class Book:
    def __init__(self, book_title, author, book_id):
        """
        Initialize a Book object with title, author, and unique ID.
        
        :param book_title: Title of the book
        :param author: Author of the book
        :param book_id: Unique identifier for the book
        """
        if not book_title or not book_title.strip():
            raise ValueError("Book title cannot be empty.")
        if not author or not author.strip():
            raise ValueError("Author name cannot be empty.")
        if not book_id or not str(book_id).strip():
            raise ValueError("Book ID cannot be empty.")
        
        self.book_title = book_title.strip()
        self.author = author.strip()
        self.book_id = str(book_id).strip()
        self.is_available = True
    
    def borrow(self):
        """
        Mark the book as borrowed if it's available.
        
        :return: True if book can be borrowed, False otherwise
        """
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self):
        """
        Mark the book as available.
        
        :return: True if book can be returned, False otherwise
        """
        if not self.is_available:
            self.is_available = True
            return True
        return False
    
    def display_details(self):
        """
        Print book details including title, author, and availability.
        """
        print(f"Book Title: {self.book_title}")
        print(f"Author: {self.author}")
        print(f"Book ID: {self.book_id}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")
        print("-" * 30)


class Member:
    def __init__(self, member_name, member_id):
        """
        Initialize a Member object with name and unique ID.
        
        :param member_name: Name of the member
        :param member_id: Unique identifier for the member
        """
        if not member_name or not member_name.strip():
            raise ValueError("Member name cannot be empty.")
        if not member_id or not str(member_id).strip():
            raise ValueError("Member ID cannot be empty.")
        
        self.member_name = member_name.strip()
        self.member_id = str(member_id).strip()
        self.borrowed_books = []
    
    def borrow_book(self, book_id):
        """
        Add a book ID to the member's borrowed books list.
        
        :param book_id: ID of the book to be borrowed
        """
        self.borrowed_books.append(str(book_id).strip())
    
    def return_book(self, book_id):
        """
        Remove a book ID from the member's borrowed books list.
        
        :param book_id: ID of the book to be returned
        :return: True if book was in borrowed list, False otherwise
        """
        book_id = str(book_id).strip()
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False
    
    def display_borrowed_books(self):
        """
        Display all books borrowed by the member.
        """
        if not self.borrowed_books:
            print(f"{self.member_name} has no borrowed books.")
        else:
            print(f"Books borrowed by {self.member_name}:")
            for book_id in self.borrowed_books:
                print(f"- Book ID: {book_id}")


class Library:
    def __init__(self, name):
        """
        Initialize a Library object with a name.
        
        :param name: Name of the library
        """
        if not name or not name.strip():
            raise ValueError("Library name cannot be empty.")
        
        self.name = name.strip()
        self.books = {}    #  create empty dictionary to contain books
        self.members = {}  #  create empty dictionary to contain members
    
    def add_book(self, book_title, author, book_id):
        """
        Add a new book to the library's catalog.
        
        :param book_title: Title of the book
        :param author: Author of the book
        :param book_id: Unique identifier for the book
        :return: True if book was added, False if book ID already exists
        """
        # Validate input
        try:
            book_id = str(book_id).strip()
            
            # Check for empty or whitespace-only inputs
            if not book_title or not book_title.strip():
                print("Error: Book title cannot be empty.")
                return False
            
            if not author or not author.strip():
                print("Error: Author name cannot be empty.")
                return False
            
            if not book_id:
                print("Error: Book ID cannot be empty.")
                return False
        
            # Check for duplicate book ID
            if book_id in self.books:
                print(f"Error: Book with ID {book_id} already exists in the library.")
                return False
            
            # Create and add the book
            new_book = Book(book_title, author, book_id)
            self.books[book_id] = new_book
            print(f"Book '{book_title}' added successfully.")
            return True
        
        except ValueError as e:
            print(f"Error adding book: {e}")
            return False
    
    def register_member(self, member_name, member_id):
        """
        Register a new member to the library.
        
        :param member_name: Name of the member
        :param member_id: Unique identifier for the member
        :return: True if member was registered, False if member ID already exists
        """
        try:
            member_id = str(member_id).strip()
            
            # Check for empty or whitespace-only inputs
            if not member_name or not member_name.strip():
                print("Error: Member name cannot be empty.")
                return False
            
            if not member_id:
                print("Error: Member ID cannot be empty.")
                return False
            
            # Check for duplicate member ID
            if member_id in self.members:
                print(f"Error: Member with ID {member_id} already exists.")
                return False
            
            # Create and register the member
            new_member = Member(member_name, member_id)
            self.members[member_id] = new_member
            print(f"Member '{member_name}' registered successfully.")
            return True
        
        except ValueError as e:
            print(f"Error registering member: {e}")
            return False
    
    def borrow_book(self, member_id, book_id):
        """
        Allow a member to borrow a book.
        
        :param member_id: ID of the member borrowing the book
        :param book_id: ID of the book to be borrowed
        :return: True if book was borrowed successfully, False otherwise
        """
        try:
            # Normalize and validate input
            member_id = str(member_id).strip()
            book_id = str(book_id).strip()
            
            # Check if member exists
            if not member_id:
                print("Error: Member ID cannot be empty.")
                return False
            
            if member_id not in self.members:
                print(f"Error: Member with ID {member_id} not found.")
                return False
            
            # Check if book exists
            if not book_id:
                print("Error: Book ID cannot be empty.")
                return False
            
            if book_id not in self.books:
                print(f"Error: Book with ID {book_id} not found.")
                return False
            
            # Proceed with borrowing
            book = self.books[book_id]
            member = self.members[member_id]
            
            if book.is_available:
                book.borrow()
                member.borrow_book(book_id)
                print(f"Book '{book.book_title}' borrowed successfully by {member.member_name}.")
                return True
            else:
                print(f"Error: Book '{book.book_title}' is currently unavailable.")
                return False
        
        except Exception as e:
            print(f"Unexpected error while borrowing book: {e}")
            return False
    
    def return_book(self, member_id, book_id):
        """
        Allow a member to return a borrowed book.
        
        :param member_id: ID of the member returning the book
        :param book_id: ID of the book to be returned
        :return: True if book was returned successfully, False otherwise
        """
        try:
            # Normalize and validate input
            member_id = str(member_id).strip()
            book_id = str(book_id).strip()
            
            # Check if member exists
            if not member_id:
                print("Error: Member ID cannot be empty.")
                return False
            
            if member_id not in self.members:
                print(f"Error: Member with ID {member_id} not found.")
                return False
            
            # Check if book exists
            if not book_id:
                print("Error: Book ID cannot be empty.")
                return False
            
            if book_id not in self.books:
                print(f"Error: Book with ID {book_id} not found.")
                return False
            
            # Proceed with returning
            book = self.books[book_id]
            member = self.members[member_id]
            
            # Check if the book was borrowed by this member
            if book_id not in member.borrowed_books:
                print(f"Error: Book '{book.book_title}' was not borrowed by {member.member_name}.")
                return False
            
            # Check if book is already available
            if book.is_available:
                print(f"Error: Book '{book.book_title}' is already in the library.")
                return False
            
            # Perform return
            member.return_book(book_id)
            book.return_book()
            print(f"Book '{book.book_title}' returned successfully by {member.member_name}.")
            return True
        
        except Exception as e:
            print(f"Unexpected error while returning book: {e}")
            return False
    
    def display_all_books(self):
        """
        Display all books in the library with their details.
        """
        print(f"Books in {self.name}:")
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books.values():
                book.display_details()
    
    def display_all_members(self):
        """
        Display all registered members.
        """
        print(f"Members of {self.name}:")
        if not self.members:
            print("No members registered.")
        else:
            for member in self.members.values():
                print(f"- {member.member_name} (ID: {member.member_id})")


def main():
    """
    Main program to interact with the IM Library Management System.
    """
    # Create the library
    try:
        im_library = Library("IM Library")
    except ValueError as e:
        print(f"Error creating library: {e}")
        return
    
    while True:
        print("\n--- IM Library Management System ---")
        print("1. Add New Book")
        print("2. Register New Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Check Book Availability")
        print("6. List All Books")
        print("7. List All Members")
        print("8. Exit")
        
        try:
            choice = input("Enter your choice (1-8): ").strip()
            
            if not choice.isdigit():
                print("Error: Please enter a number between 1 and 8.")
                continue
            
            choice = int(choice)
            
            if choice < 1 or choice > 8:
                print("Error: Please enter a number between 1 and 8.")
                continue
            
            if choice == 1:
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                book_id = input("Enter unique book ID: ").strip()
                im_library.add_book(title, author, book_id) 
                
            
            elif choice == 2:
                name = input("Enter member name: ").strip()
                member_id = input("Enter unique member ID: ").strip()
                im_library.register_member(name, member_id)
            
            elif choice == 3:
                member_id = input("Enter member ID: ").strip()
                book_id = input("Enter book ID to borrow: ").strip()
                im_library.borrow_book(member_id, book_id)
            
            elif choice == 4:
                member_id = input("Enter member ID: ").strip()
                book_id = input("Enter book ID to return: ").strip()
                im_library.return_book(member_id, book_id)
            
            elif choice == 5:
                book_id = input("Enter book ID to check availability: ").strip()
                if book_id in im_library.books:
                    im_library.books[book_id].display_details()
                else:
                    print(f"Error: Book with ID {book_id} not found in the library.")
            
            elif choice == 6:
                im_library.display_all_books()
            
            elif choice == 7:
                im_library.display_all_members()
            
            elif choice == 8:
                print("Thank you for using IM Library Management System. Goodbye!")
                break
        
        except ValueError:
            print("Error: Invalid input. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()