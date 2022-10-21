from django.contrib.auth.models import AbstractUser
from django.db import models


class name(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    gender_choices = (('M', 'male'),('F', 'female'))
    Name = models.CharField(max_length = 100)
    Moblie_number = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 1, choices = gender_choices)

class diff_field(models.Model):
    Name = models.ForeignKey(User, on_delete = models.CASCADE)
    Title = models.CharField(max_length = 100)
    Describe = models.TextField()
    Random_quantity = models.IntegerField()
    Image = models.ImageField(blank = True)
    Status = models.BooleanField()
    Date_time = models.DateTimeField()
