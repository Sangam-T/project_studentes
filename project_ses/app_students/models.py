from django.db import models
from app_courses.models import CourseModel

# Create your models here.
class SyudentModel(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    current_degree = models.CharField(max_length=200)
    profile_img = models.FileField(upload_to='students/profile/', null=True, blank=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_students'
