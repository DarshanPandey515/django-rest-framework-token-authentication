from django.db import models

# Create your models here.



class DataModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    role = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.email}"

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name
