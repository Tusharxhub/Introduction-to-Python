# 1.	Design a class LibraryCatalog to manage books. The class should have methods to add a new book (with title, author, and ISBN), check out a book, and return a book. Implement error handling for invalid ISBN formats or attempts to check out a book that is already checked out. 



from dataclasses import dataclass
from typing import Dict


# ----- Exceptions -----
class InvalidISBNError(ValueError):
    """Raised when an ISBN is malformed or fails checksum validation."""


class DuplicateISBNError(ValueError):
    """Raised when adding a book with an ISBN that already exists in the catalog."""


class BookNotFoundError(KeyError):
    """Raised when an ISBN is not found in the catalog."""


class BookAlreadyCheckedOutError(ValueError):
    """Raised when attempting to check out a book that is already checked out."""


class BookNotCheckedOutError(ValueError):
    """Raised when attempting to return a book that is not checked out."""


# ----- Data Model -----
@dataclass(frozen=True)
class Book:
    title: str
    author: str
    isbn: str  # canonical ISBN (no hyphens/spaces, uppercase X where applicable)


# ----- Catalog -----
class LibraryCatalog:
    """
    Manage a collection of books with ISBN validation and checkout state.

    Methods
    -------
    add_book(title, author, isbn) -> None
        Adds a new book. Raises InvalidISBNError for bad ISBN, DuplicateISBNError if already exists.

    checkout_book(isbn) -> None
        Checks out a book. Raises BookNotFoundError if missing,
        BookAlreadyCheckedOutError if already checked out.

    return_book(isbn) -> None
        Returns a book. Raises BookNotFoundError if missing,
        BookNotCheckedOutError if it wasn't checked out.
    """

    def __init__(self) -> None:
        self._books: Dict[str, Book] = {}          # key: canonical ISBN
        self._checked_out: Dict[str, bool] = {}    # key: canonical ISBN -> checkout state

    # ---- Public API ----
    def add_book(self, title: str, author: str, isbn: str) -> None:
        canon = self._canonical_isbn(isbn)
        if not self._is_valid_isbn(canon):
            raise InvalidISBNError(f"Invalid ISBN format/checksum: {isbn!r}")
        if canon in self._books:
            raise DuplicateISBNError(f"Book with ISBN {isbn!r} already exists.")
        self._books[canon] = Book(title=title, author=author, isbn=canon)
        self._checked_out[canon] = False

    def checkout_book(self, isbn: str) -> None:
        canon = self._canonical_isbn(isbn)
        book = self._books.get(canon)
        if book is None:
            raise BookNotFoundError(f"No book with ISBN {isbn!r} found.")
        if self._checked_out[canon]:
            raise BookAlreadyCheckedOutError(f"Book with ISBN {isbn!r} is already checked out.")
        self._checked_out[canon] = True

    def return_book(self, isbn: str) -> None:
        canon = self._canonical_isbn(isbn)
        book = self._books.get(canon)
        if book is None:
            raise BookNotFoundError(f"No book with ISBN {isbn!r} found.")
        if not self._checked_out[canon]:
            raise BookNotCheckedOutError(f"Book with ISBN {isbn!r} is not checked out.")
        self._checked_out[canon] = False

    # ---- Optional helpers ----
    def is_checked_out(self, isbn: str) -> bool:
        """Return True if the book is checked out; raises BookNotFoundError if not present."""
        canon = self._canonical_isbn(isbn)
        if canon not in self._books:
            raise BookNotFoundError(f"No book with ISBN {isbn!r} found.")
        return self._checked_out[canon]

    def get_book(self, isbn: str) -> Book:
        """Return the Book dataclass; raises BookNotFoundError if not present."""
        canon = self._canonical_isbn(isbn)
        book = self._books.get(canon)
        if book is None:
            raise BookNotFoundError(f"No book with ISBN {isbn!r} found.")
        return book

    # ---- Internal: ISBN normalization/validation ----
    @staticmethod
    def _canonical_isbn(isbn: str) -> str:
        """Remove hyphens/spaces, uppercase X (for ISBN-10)."""
        cleaned = "".join(ch for ch in isbn if ch not in {" ", "-"}).upper()
        return cleaned

    @classmethod
    def _is_valid_isbn(cls, canon: str) -> bool:
        """Validate ISBN-10 or ISBN-13 with checksum."""
        if len(canon) == 10:
            return cls._is_valid_isbn10(canon)
        if len(canon) == 13:
            return cls._is_valid_isbn13(canon)
        return False

    @staticmethod
    def _is_valid_isbn10(canon: str) -> bool:
        # Positions 1..9 must be digits; position 10 can be digit or 'X' (10)
        if not all(ch.isdigit() for ch in canon[:9]):
            return False
        if not (canon[9].isdigit() or canon[9] == "X"):
            return False
        total = 0
        for i in range(9):
            total += (10 - i) * int(canon[i])
        check_val = 10 if canon[9] == "X" else int(canon[9])
        total += check_val
        return total % 11 == 0

    @staticmethod
    def _is_valid_isbn13(canon: str) -> bool:
        if not canon.isdigit():
            return False
        digits = [int(ch) for ch in canon]
        # Compute checksum for first 12 digits
        s = 0
        for i in range(12):
            weight = 1 if i % 2 == 0 else 3
            s += weight * digits[i]
        check_digit = (10 - (s % 10)) % 10
        return check_digit == digits[12]


# ----- Example usage -----
if __name__ == "__main__":
    catalog = LibraryCatalog()

    # Add books (hyphens/spaces allowed; stored canonically)
    catalog.add_book("Clean Code", "Robert C. Martin", "978-0132350884")  # valid ISBN-13
    catalog.add_book("The Pragmatic Programmer", "Andrew Hunt, David Thomas", "0-201-61622-X")  # valid ISBN-10

    # Checkout / return flow
    catalog.checkout_book("9780132350884")
    try:
        catalog.checkout_book("978 0132350884")  # same book, different formatting -> already checked out
    except BookAlreadyCheckedOutError as e:
        print(e)

    print("Is checked out:", catalog.is_checked_out("978-0132350884"))  # True

    catalog.return_book("978-0132350884")
    print("Is checked out:", catalog.is_checked_out("978-0132350884"))  # False

    # Invalid ISBN
    try:
        catalog.add_book("Bad Book", "No Author", "123-ABC-999")
    except InvalidISBNError as e:
        print(e)
