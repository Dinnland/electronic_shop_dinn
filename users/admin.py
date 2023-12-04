from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'first_name', 'last_name', 'country', 'is_verified', 'is_active')
    search_fields = ('email', 'phone','first_name', 'last_name')
