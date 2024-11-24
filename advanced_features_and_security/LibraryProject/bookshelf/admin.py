from django.contrib import admin
from .models import Book
from .models import CustomUser
from .models import CustomUserManager
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','publication_year')
    search_fields = ('title', 'author')
    list_filter = ('title', 'author', 'publication_year')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio',)}),  # Add bio field
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio',)}),  # Add bio field for creating users
    )

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)