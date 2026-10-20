
import unittest
from book import Book
from user import User
from library import Library


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("1984", "George Orwell", 1949, "ISBN001")

    def test_book_available(self):
        self.assertFalse(self.book.borrowed)

    def test_borrow_book(self):
        self.book.borrow()
        self.assertTrue(self.book.borrowed)

    def test_borrow_twice(self):
        self.book.borrow()
        with self.assertRaises(ValueError):
            self.book.borrow()

    def test_return_book(self):
        self.book.borrow()
        self.book.return_book()
        self.assertFalse(self.book.borrowed)

    def test_return_without_borrow(self):
        with self.assertRaises(ValueError):
            self.book.return_book()


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book = Book("1984", "George Orwell", 1949, "ISBN001")
        self.user = User("Elizabeth", "U001")
        self.library.add_book(self.book)
        self.library.add_user(self.user)

    def test_borrow_integration(self):
        self.library.borrow_book("U001", "ISBN001")
        self.assertTrue(self.book.borrowed)
        self.assertEqual(len(self.user.get_history()), 1)

    def test_borrow_twice_integration(self):
        self.library.borrow_book("U001", "ISBN001")
        with self.assertRaises(ValueError):
            self.library.borrow_book("U001", "ISBN001")

    def test_return_integration(self):
        self.library.borrow_book("U001", "ISBN001")
        self.library.return_book("U001", "ISBN001")
        self.assertFalse(self.book.borrowed)


if __name__ == "__main__":
    unittest.main()
