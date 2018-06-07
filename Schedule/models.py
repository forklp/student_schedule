from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20, null=True)
    user_password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user_name


class Schdule(models.Model):
    academy = models.CharField(max_length=50, null=True)  # 开课系
    course_number = models.CharField(max_length=20, null=True)  # 课程号
    course_name = models.CharField(max_length=50, null=True)  # 课程名
    course_list = models.CharField(max_length=20, null=True)  # 课序号
    credit_hour = models.CharField(max_length=20, null=True)  # 学分
    test_type = models.CharField(max_length=20, null=True)  # 考试类型
    teacher = models.CharField(max_length=20, null=True)  # 教师
    course_week = models.CharField(max_length=20, null=True)  # 周次
    course_day = models.CharField(max_length=20, null=True)  # 星期
    course_time = models.CharField(max_length=20, null=True)  # 节次
    campus = models.CharField(max_length=20, null=True)  # 校区
    teaching_building = models.CharField(max_length=20, null=True)  # 教学楼
    classroom = models.CharField(max_length=20, null=True)  # 教室
    course_capacity = models.PositiveIntegerField(null=True)  # 课容量
    course_limit = models.CharField(max_length=50, null=True)  # 选课现在说明
    course_start = models.PositiveIntegerField(null=True)  # 课程开始节数
    course_end = models.PositiveIntegerField(null=True)  # 课程结束节数

    def __str__(self):
        return self.course_name


class User_And_Schdule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    schdule = models.ForeignKey(Schdule, on_delete=models.CASCADE, null=True)
