from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            isbn="9780743273565",
            page_count=180,
            available=True
        )

    def test_book_creation(self):
        """Test if a book is created successfully"""
        book = Book.objects.get(title="The Great Gatsby")
        self.assertEqual(book.author, "F. Scott Fitzgerald")
        self.assertEqual(book.isbn, "9780743273565")
        self.assertEqual(book.page_count, 180)
        self.assertTrue(book.available)
