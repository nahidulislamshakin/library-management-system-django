from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(BaseUserAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']

# Unregister the default User admin
admin.site.unregister(User)

# Register the User model with the custom admin configuration
admin.site.register(User, CustomUserAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author", "isbn"]  

  
admin.site.register(Book, BookAdmin)

class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ["id", "student_id", "isbn"]  
  
admin.site.register(IssuedBook, IssuedBookAdmin)


class StudentBookAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "roll_no"]  
  
admin.site.register(Student, StudentBookAdmin)