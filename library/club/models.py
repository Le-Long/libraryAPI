from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Book(models.Model):
    """Model representing a book."""
    bookID = models.CharField(primary_key=True, max_length=12)
    quantity = models.IntegerField()
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.bookID)])
# Create your models here.


class Student(models.Model) :
    """Model representing a student"""
    studentID = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=100)
    dob = models.DateField("Date of Birth", null=True, blank=True)
    faculty = models.CharField(max_length=100)
    gender = models.CharField(choices=(("M","Nam"), ("F","Nữ")), max_length=1)
    status = models.CharField(choices=(("debt","Nợ"), ("free","Không nợ")), max_length=4)
    note = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this student."""
        return reverse('student-detail', args=[str(self.studentID)])


class BookLog(models.Model) :
    """Model representing history of activities"""
    student = models.ForeignKey("Student", on_delete=models.PROTECT)
    book = models.ForeignKey("Book", on_delete=models.PROTECT)
    borrowingDate = models.DateField()
    returningDate = models.DateField(null=True, blank=True)
    status = models.CharField(choices=(("free","Đã trả"), ("debt", "Chưa trả")), max_length=4)
    supervisor = models.CharField(max_length=100)

    class Meta:
        ordering = ['borrowingDate']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.student.name} ({self.book.title})'


'''class User(models.Model) :
    """Model representing an admin"""
    userID = models.UUIDField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(choices=(("BCN","BCN"), ("mem", "trực viên")), max_length=3)

    def __str__(self):
        """String for representing the Model object."""
        return self.username'''


class Member(models.Model) :
    "Model representing a club member"
    memberID = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    gen = models.SmallIntegerField("generation")
    dob = models.DateField("Date of Birth", null=True, blank=True)
    gender = models.CharField(choices=(("M","Nam"), ("F","Nữ")), max_length=1)
    year = models.SmallIntegerField("Niên khóa")
    fb = models.TextField("tài khoản facebook")
    section = models.CharField(choices=(("T", "Truyền thông"),
                                        ("S", "Sự kiện"),
                                        ("P", "Phục vụ bạn đọc")), max_length=30)
    role = models.CharField(choices=(("mem", "Thành viên"),
                                     ("viceMod", "Phó ban"),
                                     ("mod", "Trưởng ban"),
                                     ("treasurer", "Thủ quỹ"),
                                     ("viceSupermod", "Phó Chủ nhiệm"),
                                     ("supermod", "Chủ nhiệm")), max_length=30)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

