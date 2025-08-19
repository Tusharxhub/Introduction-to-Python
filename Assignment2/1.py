# 1.	Design a class LibraryCatalog to manage books. The class should have methods to add a new book (with title, author, and ISBN), check out a book, and return a book. Implement error handling for invalid ISBN formats or attempts to check out a book that is already checked out. 



import re

class LibraryCatalog:
    """
    Manages a collection of books in a library.
    
    This class allows adding new books, checking them out, and returning them.
    It uses a dictionary to store books, with the ISBN as the key.
    """
    def __init__(self):
        """Initializes an empty library catalog."""
        self.books = {}

    def _clean_isbn(self, isbn):
        """Removes hyphens and whitespace from an ISBN string."""
        return isbn.replace("-", "").strip()

    def _is_valid_isbn(self, isbn):
        """
        Validates the ISBN format.
        
        A valid ISBN must be 10 or 13 digits long after removing hyphens.
        """
        cleaned_isbn = self._clean_isbn(isbn)
        return cleaned_isbn.isdigit() and len(cleaned_isbn) in [10, 13]

    def add_book(self, title, author, isbn):
        """
        Adds a new book to the catalog.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.

        Raises:
            ValueError: If the ISBN format is invalid or the book already exists.
        """
        if not self._is_valid_isbn(isbn):
            raise ValueError(f"Error: Invalid ISBN format for '{isbn}'. Must be 10 or 13 digits.")
        
        cleaned_isbn = self._clean_isbn(isbn)
        if cleaned_isbn in self.books:
            raise ValueError(f"Error: Book with ISBN {cleaned_isbn} already exists.")
            
        self.books[cleaned_isbn] = {
            "title": title,
            "author": author,
            "status": "available"
        }
        print(f"Success: '{title}' by {author} added to the catalog.")

    def checkout_book(self, isbn):
        """
        Checks out a book, marking its status as 'checked out'.

        Args:
            isbn (str): The ISBN of the book to check out.

        Raises:
            KeyError: If no book with the given ISBN is found.
            ValueError: If the book is already checked out.
        """
        cleaned_isbn = self._clean_isbn(isbn)
        if cleaned_isbn not in self.books:
            raise KeyError(f"Error: Book with ISBN {cleaned_isbn} not found.")

        book = self.books[cleaned_isbn]
        if book["status"] == "checked out":
            raise ValueError(f"Error: '{book['title']}' is already checked out.")
        
        book["status"] = "checked out"
        print(f"Success: '{book['title']}' has been checked out.")

    def return_book(self, isbn):
        """
        Returns a book, marking its status as 'available'.

        Args:
            isbn (str): The ISBN of the book to return.

        Raises:
            KeyError: If no book with the given ISBN is found.
            ValueError: If the book is already available.
        """
        cleaned_isbn = self._clean_isbn(isbn)
        if cleaned_isbn not in self.books:
            raise KeyError(f"Error: Book with ISBN {cleaned_isbn} not found.")

        book = self.books[cleaned_isbn]
        if book["status"] == "available":
            raise ValueError(f"Error: '{book['title']}' is already available.")
            
        book["status"] = "available"
        print(f"Success: '{book['title']}' has been returned.")

    def display_catalog(self):
        """Prints the current status of all books in the catalog."""
        print("\n--- Library Catalog Status ---")
        if not self.books:
            print("The catalog is empty.")
            return
        for isbn, details in self.books.items():
            print(
                f"ISBN: {isbn} | Title: {details['title']} | "
                f"Author: {details['author']} | Status: {details['status']}"
            )
        print("----------------------------\n")