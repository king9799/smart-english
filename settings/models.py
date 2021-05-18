from django.db import models
from django.conf import settings


class Student(models.Model):
    full_name = models.CharField(max_length=255)


class Timetable(models.Model):
    subject_name = models.CharField(max_length=255)
    lesson_pattern = models.CharField(max_length=255)
    lesson_type = models.CharField(max_length=255)
    group_type = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'Profile for user {{ self.user.username}}'    


class Building(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    room_amount = models.IntegerField(default=0)
    nickname = models.CharField(max_length=255)
    added_time = models.DateTimeField(auto_now_add=True)


