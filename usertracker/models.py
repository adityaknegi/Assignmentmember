from django.db import models

# Create your models here.


class User(models.Model):
    user_first_name = models.CharField(max_length=50, blank=False, default='')
    user_last_name = models.CharField(max_length=50, blank=False, default='')
    user_email = models.EmailField(max_length=250, blank=False, default='')
    user_hash = models.CharField(max_length=50, blank=False, default='')
    time_zone = models.CharField(max_length=50, blank=False, default='')
    user_created_on = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=50, blank=False, default='')
    end_time = models.CharField(max_length=50, blank=False, default='')
    updated_on = models.DateTimeField(auto_now_add=True)
