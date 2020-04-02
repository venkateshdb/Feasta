from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    filter_horizontal = ()
    list_filter = ()
    
    fieldsets = (
        (None, {'fields': ('phone_no', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_user', 'is_shop'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_no', 'password1', 'password2'),
        }),
    )

    list_display = ('phone_no', 'email', 'first_name', 'last_name', 'is_staff', 'is_user', 'is_shop')
    search_fields = ('phone_no', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('phone_no',)

admin.site.register(CustomUser, CustomUserAdmin)