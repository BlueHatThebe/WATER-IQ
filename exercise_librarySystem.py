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
            print(f"\nBook '{self.book_title}' has been marked as borrowed.\n")
            return True
        print(f"\nBook '{self.book_title}' is not available for borrowing.\n")
        return False
    
    def return_book(self):
        """
        Mark the book as available.
        
        :return: True if book can be returned, False otherwise
        """
        if not self.is_available:
            self.is_available = True
            print(f"\nBook '{self.book_title}' has been marked as returned.\n")
            return True
        print(f"\nBook '{self.book_title}' is already available.\n")
        return False
    
    def display_details(self):
        """
        Print book details including title, author, and availability.
        """
        print(f"\nBook Title: {self.book_title}")
        print(f"Author: {self.author}")
        print(f"Book ID: {self.book_id}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")
        print("-" * 30 + "\n")


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
        book_id = str(book_id).strip()
        self.borrowed_books.append(book_id)
        print(f"\nBook ID {book_id} added to {self.member_name}'s borrowed list.\n")
    
    def return_book(self, book_id):
        """
        Remove a book ID from the member's borrowed books list.
        
        :param book_id: ID of the book to be returned
        :return: True if book was in borrowed list, False otherwise
        """
        book_id = str(book_id).strip()
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            print(f"\nBook ID {book_id} removed from {self.member_name}'s borrowed list.\n")
            return True
        print(f"\nBook ID {book_id} not found in {self.member_name}'s borrowed list.\n")
        return False
    
    def display_borrowed_books(self):
        """
        Display all books borrowed by the member.
        """
        print(f"\nBooks borrowed by {self.member_name}:")
        if not self.borrowed_books:
            print("No borrowed books.\n")
        else:
            for book_id in self.borrowed_books:
                print(f"- Book ID: {book_id}")
            print()


class Library:
    def __init__(self, name):
        """
        Initialize a Library object with a name.
        
        :param name: Name of the library
        """
        if not name or not name.strip():
            raise ValueError("Library name cannot be empty.")
        
        self.name = name.strip()
        self.books = {}
        self.members = {}
    
    def add_book(self, book_title, author, book_id):
        """
        Add a new book to the library's catalog.
        
        :param book_title: Title of the book
        :param author: Author of the book
        :param book_id: Unique identifier for the book
        :return: True if book was added, False if book ID already exists
        """
        try:
            book_id = str(book_id).strip()
            
            if not book_title or not book_title.strip():
                print("\nError: Book title cannot be empty.\n")
                return False
            
            if not author or not author.strip():
                print("\nError: Author name cannot be empty.\n")
                return False
            
            if not book_id:
                print("\nError: Book ID cannot be empty.\n")
                return False
        
            if book_id in self.books:
                print(f"\nError: Book with ID {book_id} already exists in the library.\n")
                return False
            
            new_book = Book(book_title, author, book_id)
            self.books[book_id] = new_book
            print(f"\nBook '{book_title}' added successfully to {self.name}.\n")
            return True
        
        except ValueError as e:
            print(f"\nError adding book: {e}\n")
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
            
            if not member_name or not member_name.strip():
                print("\nError: Member name cannot be empty.\n")
                return False
            
            if not member_id:
                print("\nError: Member ID cannot be empty.\n")
                return False
            
            if member_id in self.members:
                print(f"\nError: Member with ID {member_id} already exists.\n")
                return False
            
            new_member = Member(member_name, member_id)
            self.members[member_id] = new_member
            print(f"\nMember '{member_name}' registered successfully in {self.name}.\n")
            return True
        
        except ValueError as e:
            print(f"\nError registering member: {e}\n")
            return False
    
    def borrow_book(self, member_id, book_id):
        """
        Allow a member to borrow a book.
        
        :param member_id: ID of the member borrowing the book
        :param book_id: ID of the book to be borrowed
        :return: True if book was borrowed successfully, False otherwise
        """
        try:
            member_id = str(member_id).strip()
            book_id = str(book_id).strip()
            
            if not member_id:
                print("\nError: Member ID cannot be empty.\n")
                return False
            
            if member_id not in self.members:
                print(f"\nError: Member with ID {member_id} not found.\n")
                return False
            
            if not book_id:
                print("\nError: Book ID cannot be empty.\n")
                return False
            
            if book_id not in self.books:
                print(f"\nError: Book with ID {book_id} not found.\n")
                return False
            
            book = self.books[book_id]
            member = self.members[member_id]
            
            if book.is_available:
                book.borrow()
                member.borrow_book(book_id)
                print(f"\nBook '{book.book_title}' borrowed successfully by {member.member_name}.\n")
                return True
            else:
                print(f"\nError: Book '{book.book_title}' is currently unavailable.\n")
                return False
        
        except Exception as e:
            print(f"\nUnexpected error while borrowing book: {e}\n")
            return False
    
    def return_book(self, member_id, book_id):
        """
        Allow a member to return a borrowed book.
        
        :param member_id: ID of the member returning the book
        :param book_id: ID of the book to be returned
        :return: True if book was returned successfully, False otherwise
        """
        try:
            member_id = str(member_id).strip()
            book_id = str(book_id).strip()
            
            if not member_id:
                print("\nError: Member ID cannot be empty.\n")
                return False
            
            if member_id not in self.members:
                print(f"\nError: Member with ID {member_id} not found.\n")
                return False
            
            if not book_id:
                print("\nError: Book ID cannot be empty.\n")
                return False
            
            if book_id not in self.books:
                print(f"\nError: Book with ID {book_id} not found.\n")
                return False
            
            book = self.books[book_id]
            member = self.members[member_id]
            
            if book_id not in member.borrowed_books:
                print(f"\nError: Book '{book.book_title}' was not borrowed by {member.member_name}.\n")
                return False
            
            if book.is_available:
                print(f"\nError: Book '{book.book_title}' is already in the library.\n")
                return False
            
            member.return_book(book_id)
            book.return_book()
            print(f"\nBook '{book.book_title}' returned successfully by {member.member_name}.\n")
            return True
        
        except Exception as e:
            print(f"\nUnexpected error while returning book: {e}\n")
            return False
    
    def display_all_books(self):
        """
        Display all books in the library with their details.
        """
        print(f"\nBooks in {self.name}:")
        if not self.books:
            print("No books in the library.\n")
        else:
            for book in self.books.values():
                book.display_details()
    
    def display_all_members(self):
        """
        Display all registered members.
        """
        print(f"\nMembers of {self.name}:")
        if not self.members:
            print("No members registered.\n")
        else:
            for member in self.members.values():
                print(f"- {member.member_name} (ID: {member.member_id})")
            print()


def main():
    """
    Main program to interact with the IM Library Management System.
    """
    try:
        im_library = Library("IM Library")
        print("\nIM Library Management System initialized successfully.\n")
    except ValueError as e:
        print(f"\nError creating library: {e}\n")
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
        print("8. Exit\n")
        
        try:
            choice = input("Enter your choice (1-8): ").strip()
            
            if not choice:
                print("\nError: Choice cannot be empty.\n")
                continue
            
            if not choice.isdigit():
                print("\nError: Please enter a number between 1 and 8.\n")
                continue
            
            choice = int(choice)
            
            if choice < 1 or choice > 8:
                print("\nError: Please enter a number between 1 and 8.\n")
                continue
            
            if choice == 1:
                title = input("\nEnter book title: ").strip()
                author = input("Enter book author: ").strip()
                book_id = input("Enter unique book ID: ").strip()
                if not all([title, author, book_id]):
                    print("\nError: All fields must be non-empty.\n")
                else:
                    im_library.add_book(title, author, book_id)
                
            elif choice == 2:
                name = input("\nEnter member name: ").strip()
                member_id = input("Enter unique member ID: ").strip()
                if not all([name, member_id]):
                    print("\nError: All fields must be non-empty.\n")
                else:
                    im_library.register_member(name, member_id)
            
            elif choice == 3:
                member_id = input("\nEnter member ID: ").strip()
                book_id = input("Enter book ID to borrow: ").strip()
                if not all([member_id, book_id]):
                    print("\nError: All fields must be non-empty.\n")
                else:
                    im_library.borrow_book(member_id, book_id)
            
            elif choice == 4:
                member_id = input("\nEnter member ID: ").strip()
                book_id = input("Enter book ID to return: ").strip()
                if not all([member_id, book_id]):
                    print("\nError: All fields must be non-empty.\n")
                else:
                    im_library.return_book(member_id, book_id)
            
            elif choice == 5:
                book_id = input("\nEnter book ID to check availability: ").strip()
                if not book_id:
                    print("\nError: Book ID cannot be empty.\n")
                elif book_id in im_library.books:
                    im_library.books[book_id].display_details()
                else:
                    print(f"\nError: Book with ID {book_id} not found in the library.\n")
            
            elif choice == 6:
                im_library.display_all_books()
            
            elif choice == 7:
                im_library.display_all_members()
            
            elif choice == 8:
                print("\nThank you for using IM Library Management System. Goodbye!\n")
                break
        
        except ValueError:
            print("\nError: Invalid input. Please try again.\n")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}\n")


if __name__ == "__main__":
    main()