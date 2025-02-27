from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Loan
from .serializers import LoanSerializer
from books.models import Book
from datetime import datetime

class BorrowBookView(generics.CreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]  #  Only authenticated users can borrow

    def post(self, request, *args, **kwargs):
        book_id = request.data.get('book_id')
        try:
            book = Book.objects.get(id=book_id, available=True)
            loan = Loan.objects.create(user=request.user, book=book)
            book.available = False  # Book now marked as unavailable
            book.save()
            return Response(LoanSerializer(loan).data, status=status.HTTP_201_CREATED)
        except Book.DoesNotExist:
            return Response({"error": "Book not available or does not exist."}, status=status.HTTP_400_BAD_REQUEST)


class ReturnBookView(generics.GenericAPIView):
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]  #  Only authenticated users can return

    def post(self, request, book_id):
        try:
            # Find the latest active loan (not returned yet) for the given book by the logged-in user
            loan = Loan.objects.filter(book_id=book_id, user=request.user, returned_at__isnull=True).latest('borrowed_at')
            loan.returned_at = datetime.now()
            loan.book.available = True  # Book now marked as available
            loan.book.save()
            loan.save()
            return Response({"message": "Book returned successfully!", "loan": LoanSerializer(loan).data}, status=status.HTTP_200_OK)
        
        except Loan.DoesNotExist:
            return Response({"error": "No active loan found for this book or it’s already returned."}, status=status.HTTP_400_BAD_REQUEST)