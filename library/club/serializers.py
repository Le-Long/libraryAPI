from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class StudentSerializer(serializers.ModelSerializer):
    history = serializers.HyperlinkedRelatedField(view_name='book_log', read_only=True)

    class Meta:
        model = Student
        fields = ['studentID', 'name', 'dob', 'faculty', 'gender', 'status', 'history']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['bookID', 'title', 'price']


class BookLogSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(view_name='book', read_only=True)

    class Meta:
        model = BookLog
        fields = ['book', 'student', 'borrowingDate', 'returningDate']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['name', 'gen', 'dob', 'section', 'role']