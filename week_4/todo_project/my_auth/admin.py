from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from my_auth.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'second_name', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )
