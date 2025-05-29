from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['no','name','major']

admin.site.register(Student,StudentAdmin)