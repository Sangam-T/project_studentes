from django.contrib import admin
from app_courses.models import CourseModel
# Register your models here.
class CourseModelAdmin(admin.ModelAdmin):
    list_filter = ("course_name", "course_code")
    search_fields = ("course_name", "course_code")
    list_display = ("course_name", "course_code")

admin.site.register(CourseModel)

admin.site.site_header = "Student Enquiry System"
admin.site.side_title = "SES"
admin.site.index_title = "Admin Pannel"