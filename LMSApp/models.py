from django.db import models
from django.forms import forms


# Create your models here.
class Course(models.Model):
    Course_Name = models.CharField(max_length=40, default=None)

    def __str__(self):
        return f'{self.Course_Name}'


class Book(models.Model):
    Book_Name = models.CharField(max_length=40, default=None)
    Author_Name = models.CharField(max_length=40, default=None)
    Course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Book_Name}'


class Student(models.Model):
    Stud_Name = models.CharField(max_length=40, default=None)
    Stud_Phn_No = models.BigIntegerField(default=0)
    Stud_Sem = models.IntegerField(default=0)
    Stud_Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Stud_Password = models.CharField(max_length=40, default=None)
    is_logged_in = models.CharField(max_length=40, default='No')
    def __str__(self):
        return f'{self.Stud_Name}'


class Issue_Book(models.Model):
    Stud_Name = models.ForeignKey(Student, on_delete=models.CASCADE)
    Book_Name = models.ForeignKey(Book, on_delete=models.CASCADE)
    Start_Date = models.DateField()
    End_Date = models.DateField()




