from django import forms
from app_courses.models import CourseModel

class CourseCreateForm(forms.ModelForm):
    class Meta:
        fields = ("course_name", "course_code")
        model = CourseModel