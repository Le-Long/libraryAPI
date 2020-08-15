# libraryAPI
Restful API for the web of the library club. Address: https://protected-hollows-90691.herokuapp.com

Run:
- Require Python 3, Django and djangorestframework
- Change DATABASE in settings.py
- Sync your database:
  py manage.py migrate
- Create superuser:
  py manage.py createsuperuser
- Run local server:
  py manage.py runserver

Endpoint
- Student:

  /club/students (GET, POST): list all students or create a new one
  
  /club/students/:id (GET, PUT, PATCH, DELETE): work with a separate student
  
  /club/students/:id/history (GET): list all book log that the student has not returned yet (only if the student's status is 'debt') 

- Book:

  /club/books (GET, POST): list all books or create a new one
  
  /club/books/:id (GET, PUT, PATCH, DELETE): work with a separate book
  
- Book Log:

  /club/booklog (GET, POST): list all book logs or create a new one
  
- User:

  /club/students (GET, POST): list all users or create a new one
  
  /club/students/:id (GET, PUT, PATCH, DELETE): work with a separate user
  
- Member:

  /club/students (GET, POST): list all members or create a new one
  
  /club/students/:id (GET, PUT, PATCH, DELETE): work with a separate member
  
- Auth:

  /club/api-auth/login (POST): log in
  
  /club/api-auth/logout (GET): log out
  
- Admin
