from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    gender_choices = (('M', 'male'), ('F', 'female'))
    Moblie_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=gender_choices)

class to_do_list_model(models.Model):
    assign_to = models.ManyToManyField(user, through = 'list_member')
    task_title = models.CharField(max_length = 100)
    description = models.TextField()
    related_quantity = models.IntegerField()
    related_image = models.ImageField(blank = True)
    task_status = models.BooleanField()
    end_date = models.DateTimeField()

    def assigned_to(self):
        return ','.join([str(p) for p in self.assign_to.all()])

class list_member(models.Model):
    to_do = models.ForeignKey(to_do_list_model, on_delete = models.CASCADE)
    uni_user = models.ForeignKey(user, on_delete = models.CASCADE)