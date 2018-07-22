from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(Author, null=True,
    related_name='books', on_delete=models.SET_NULL)

    genres = models.ManyToManyField(Genre,
     related_name='books')

    rate = models.FloatField()

    def __str__(self):
        return f'{self.title} :: {self.author} [{self.rate}]'
