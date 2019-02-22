from django.db import models

# Create your models here.
# name, pageNumber, genre, and publishDate
class Book(models.Model):
    name = models.CharField(max_length=200)
    pageNumber = models.IntegerField(default=0)
    genre = models.CharField(max_length=200)
    publishDate = models.DateField()

    def __str__(self):
        return f"{self.name} that's {self.genre} with {self.pageNumber} pages"


# make, model, and year attributes.
class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"