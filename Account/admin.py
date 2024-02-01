from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

# admin.site.register(CustomUser, UserAdmin)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')  # Add the new fields here

    def custom_field(self, obj):
        # Logic to generate the custom field value
        return obj.username 

    custom_field.short_description = 'Custom Field'  # Optional: Set a custom column header for the field


class CustomUserAdmin(YourModelAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')  # Add the new fields here

admin.site.register(CustomUser, CustomUserAdmin)
