from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserRegistrationForm, UserUpdatingForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(BaseUserAdmin):

    form = UserUpdatingForm
    add_form = UserRegistrationForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (
            None, {'fields': ('email', 'password')}
        ),
        (
            'Personal Info', {'fields': ('first_name', 'last_name', 'image', 'gender')}
        ),
        (
            'Permissions',
            {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
            }
        )
    )

    add_fieldsets = (
        (
            None,
            {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
            }
        ),
    )

admin.site.register(User, UserAdmin)