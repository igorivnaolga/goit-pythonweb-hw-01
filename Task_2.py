from abc import ABC, abstractmethod
from typing import List
from logger import logger


# SRP (Single Responsibility Principle): a separate Book class to store book data
class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# ISP (Interface Segregation Principle): clear interface for library operations
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


# OCP (Open/Closed Principle): Library class can be extended (via inheritance, decorators, etc.)
# LSP (Liskov Substitution Principle): fully implements LibraryInterface and can be safely substituted
class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        logger.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        original_count = len(self._books)
        self._books = [book for book in self._books if book.title != title]
        if len(self._books) < original_count:
            logger.info(f"Book removed: {title}")
        else:
            logger.info(f"Book not found: {title}")

    def get_books(self) -> List[Book]:
        return self._books


# DIP (Dependency Inversion Principle): LibraryManager depends on abstractions, not concrete implementations
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logger.info("Library is empty.")
        for book in books:
            logger.info(str(book))


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
