
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from django.contrib.auth.models import Group
from django.utils.html import format_html




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('first_name','last_name','email', 'username', 'restaurant', 'is_restaurant_user', 'is_superuser')
    fieldsets = (
        ('Main Information', {
            'fields': ('first_name','last_name','email', 'username', 'restaurant', 'is_restaurant_user', 'is_superuser'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email', 'username','password1', 'password2', 'is_restaurant_user', 'is_superuser')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)