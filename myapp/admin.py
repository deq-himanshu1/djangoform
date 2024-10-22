from django.contrib import admin
from .models import UserProfile, Address
# Register your models here.

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1  # Number of empty forms to display

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address')
    inlines = [AddressInline]

admin.site.register(UserProfile)