from django.urls import path
from .views import BorrowBookView, ReturnBookView

urlpatterns = [
    path('borrow/', BorrowBookView.as_view(), name='borrow-book'),        # Borrow endpoint
    path('return/<int:book_id>/', ReturnBookView.as_view(), name='return-book'), # Return endpoint
]
