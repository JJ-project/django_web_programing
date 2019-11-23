from django.contrib import admin
from books.models import Book, Author, Publisher
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)

#등록하면 cmd창에서 py manage.py makemigrations  -->  py manage.py migrate