from django.db import models

from django.core.validators import MaxValueValidator
# Create your models here.

class Student(models.Model):
    StudentID = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Year = models.IntegerField(validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.StudentID

class Faculty(models.Model):
    FacultyID = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)

    def __str__(self):
        return self.FacultyID

class Project(models.Model):
    Name = models.CharField(max_length=300)
    Description = models.CharField(max_length=300)
    Deadline = models.DateTimeField("deadline")
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Students = models.ManyToManyField(Student)

    def __str__(self):
        return self.Name

class Papers(models.Model):
    Title = models.CharField(max_length=300)
    Description = models.CharField(max_length=300)
    SubmissionDate = models.DateTimeField("submission")
    Authors = models.ManyToManyField(Student)
    Mentor = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

class Feedback(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Feedback = models.CharField(max_length=300)
    Rating = models.IntegerField()

    def __str__(self):
        return self.Feedback