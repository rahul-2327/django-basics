from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('CH', 'CHOCOLATE'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai/')
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

# one to many


class ChaiReviews(models.Model):
    chai = models.ForeignKey(
        ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f'{self.user.username} review for {self.chai}'


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    chai_varities = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name


# one to one
class ChaiCertificate(models.Model) :
    pass