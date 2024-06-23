from django.urls import path
from book_app.views import BookListCreateView, BookRetrieveUpdateDestroyView, AuthorListCreateView, AuthorRetrieveUpdateDestroyView

urlpatterns = [
    # 작가
    path("authors", AuthorListCreateView.as_view(), name="author-list-create"),
    path("authors/<int:pk>", AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail-update-destroy'),
    # 책
    path("books", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>", BookRetrieveUpdateDestroyView.as_view(), name='book-detail-update-destroy'),
]