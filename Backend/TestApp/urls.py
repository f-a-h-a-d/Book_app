from django.template.defaulttags import url
from django.urls import path, include

from knox import views as knox_views
from rest_framework import routers

from TestApp.views import CreateUserView, LoginView, ManageUserView, AddNewBookView, ListAllBooksView, GetBookByIdView, \
    AddNewAuthor, ListAllAuthorsView

app_name = 'TestApp'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name="create"),
    path('profile/', ManageUserView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),

    path('books/add/', AddNewBookView.as_view(), name='add_new_book'),
    path('books/list/', ListAllBooksView.as_view(), name='list_all_books'),
    path('books/<int:id>/', GetBookByIdView.as_view(), name='get_book_by_id'),

    path('author/add/', AddNewAuthor.as_view(), name='add_new_author'),
    path('author/list/', ListAllAuthorsView.as_view()),
    #path('author/books/bookimage/', StoreBookImage.as_view(), name='store_book_image')



]