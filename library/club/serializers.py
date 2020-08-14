from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['studentID', 'name', 'dob', 'faculty', 'gender', 'status']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'bookID', 'title', 'price']


class BookLogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BookLog
        fields = ['url', 'book', 'student', 'borrowingDate', 'returningDate']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['name', 'gen', 'dob', 'section', 'role']