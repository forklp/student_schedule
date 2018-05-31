from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20, null=True)
    user_password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user_name


class Schdule(models.Model):
    academy = models.CharField(max_length=50, null=True)
    course_number = models.CharField(max_length=20, null=True)
    course_name = models.CharField(max_length=50, null=True)
    course_list = models.CharField(max_length=20, null=True)
    credit_hour = models.CharField(max_length=20, null=True)
    test_type = models.CharField(max_length=20, null=True)
    teacher = models.CharField(max_length=20, null=True)
    course_week = models.CharField(max_length=20, null=True)
    course_day = models.CharField(max_length=20, null=True)
    course_time = models.CharField(max_length=20, null=True)
    campus = models.CharField(max_length=20, null=True)
    teaching_building = models.CharField(max_length=20, null=True)
    classroom = models.CharField(max_length=20, null=True)
    course_capacity = models.PositiveIntegerField(null=True)
    course_limit = models.CharField(max_length=50, null=True)
    course_start = models.PositiveIntegerField(null=True)
    course_end = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.course_name


class User_And_Schdule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    schdule = models.ForeignKey(Schdule, on_delete=models.CASCADE, null=True)