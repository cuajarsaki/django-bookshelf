from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('create/', views.BookCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('', views.BookListView.as_view(), name='book_list'),
]
