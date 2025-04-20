from django.contrib import admin
from .models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','roll', 'age', 'father_name', 'mother_name', 'gender']
    search_fields = ['name','roll', 'age' 'father_name', 'mother_name', 'gender''name', 'father_name']
admin.site.register(Student, StudentAdmin)