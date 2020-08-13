from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BookLog.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# Create your views here.
