# django imports
from django.contrib.auth import login
from knox.models import AuthToken

# rest_framework imports
from rest_framework import generics, authentication, permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer

# knox imports
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

from TestApp.models import Book, Author
# local apps import
from TestApp.serializers import UserSerializer, AuthSerializer, BookSerializer, AuthorSerializer

from rest_framework.authentication import SessionAuthentication

from rest_framework.parsers import MultiPartParser, FormParser

class CreateUserView(generics.CreateAPIView):
    # Create user API view
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginView(KnoxLoginView):
    # login view extending KnoxLoginView
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user



class AddNewAuthor(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AddNewBookView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ListAllBooksView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListAllAuthorsView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GetBookByIdView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


# class StoreBookImage(CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

