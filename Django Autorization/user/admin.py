from django.contrib import admin
from .models import Student, Profile


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'city', 'image', 'user']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'image']