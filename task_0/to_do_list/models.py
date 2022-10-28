from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    gender_choices = (('M', 'male'), ('F', 'female'))
    Moblie_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=gender_choices)
    profile_picture = models.ImageField(upload_to='media/profile_images/', blank=True)


class to_do_list_models(models.Model):
    assign_to = models.ManyToManyField(user, through='list_member')
    task_title = models.CharField(max_length=100)
    description = models.TextField()
    related_image = models.ImageField(upload_to='media/related_image/', blank=True)
    end_date = models.DateTimeField()

    def assigned_to(self):
        return ','.join([str(p) for p in self.assign_to.all()])


class list_member(models.Model):
    to_do = models.ForeignKey(to_do_list_models, on_delete=models.CASCADE)
    uni_user = models.ForeignKey(user, on_delete=models.CASCADE)
