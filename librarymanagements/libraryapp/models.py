from django.db import models

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=40)
    def __str__(self):
        return f'{self.course_name}'
class Book(models.Model):
    b_name=models.CharField(max_length=50)
    a_name=models.CharField(max_length=50)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.b_name}'

class Student(models.Model):
    s_name=models.CharField(max_length=50)
    s_password=models.CharField(max_length=50)
    s_phone=models.BigIntegerField()
    s_semester=models.IntegerField()
    s_course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.s_name}'



class Issue_book(models.Model):
    std_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    bk_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    i_date = models.DateField()
    e_date = models.DateField()