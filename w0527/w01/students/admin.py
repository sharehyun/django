from django.contrib import admin
from students.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','major','age']

admin.site.register(Student)