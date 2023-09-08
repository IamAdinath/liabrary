from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    def __str__(self):
        return self.name

class Bookshelf(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_time = models.DateTimeField(auto_now=True)
    assigned_status = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class RentRates(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name

class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.user