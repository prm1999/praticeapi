from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import UserProfile, Crop
from django.contrib.auth import get_user_model


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm

    #model = get_user_model()
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'groups')
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password',)
        }),
        ('Personal', {
            'fields':
                ('first_name',  'mobile_no', 'address', 'email_id', 'date_of_birth')
        }),
        ('Permissions', {
            'fields':
                ('is_active', 'is_staff', 'is_superuser', 'groups')
        }),
        ('Important dates',
         {'fields':
              ('last_login', 'date_joined')
          }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(UserProfile, UserAdmin)
admin.site.register(Crop)

# Register your models here.
