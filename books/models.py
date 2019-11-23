from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author') #Book테이블과 Author테이블은 N:N관계(ManyToManyField)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)  #Book테이블과 Publisher테이블은 N:1관계(ForeignKey), on_delete는 하나의 Publisher레코드가 삭제되면 그것과 연결된 Book테이블의 레코들도 삭제된다는 의미
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

