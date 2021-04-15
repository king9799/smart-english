from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=255)


class Timetable(models.Model):
    subject_name = models.CharField(max_length=255)
    lesson_pattern = models.CharField(max_length=255)
    lesson_type = models.CharField(max_length=255)
    group_type = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    

