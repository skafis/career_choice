from django.contrib import admin

from course.models import Courses, Course_instructor, Learners
# Register your models here.
admin.site.register (Courses)
admin.site.register (Course_instructor)
admin.site.register (Learners)