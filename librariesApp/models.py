from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

# Create your models here.
class Library(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.username}'s Library"

class LibraryItem(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    added = models.TimeField(null=True ,auto_now_add=True)

    def __str__(self):
        return self.course.course_name