from django.contrib import admin
from .models import Papers,Faculty,Feedback,Project,Student
# Register your models here.

admin.site.register(Papers)
admin.site.register(Faculty)
admin.site.register(Feedback)
admin.site.register(Project)
admin.site.register(Student)