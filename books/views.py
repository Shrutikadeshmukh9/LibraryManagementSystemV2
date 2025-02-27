from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from .models import Book
from .serializers import BookSerializer


# Pagination: Controls how many books appear per page
class BookPagination(PageNumberPagination):
    page_size = 5  # Default number of books per page
    page_size_query_param = 'page_size'
    max_page_size = 10


# List View: Now with filtering and pagination
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anonymous users can view books
    pagination_class = BookPagination  # Pagination added
    filter_backends = [filters.SearchFilter]  # Enable filtering
    search_fields = ['title', 'author', 'available']  # Filter by title, author, availability


# Create Book: Only admins can add
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]  # Admin-only access


# Retrieve Book Details
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Everyone can view


# Update Book: Admin access only
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]


# Delete Book: Admin access only
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]
