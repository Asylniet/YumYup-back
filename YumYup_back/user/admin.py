from django.contrib import admin
from user.models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'password']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'phone_number', 'bio', 'avatar']
# Register your models here.


# Register your models here.
