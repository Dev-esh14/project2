from django.contrib import admin
from .models import Department, Student, Staff, Bonafide 
# Register your models here.

admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Bonafide)
admin.site.register(Department)
