from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from twitteruser.models import TwitterUser

# Register your models here.


ADDITIONAL_USER_FIELD = (
    (None, {'fields': ('name', 'follow')}),
)


class CustomUserAdmin(UserAdmin):
    view = ['username', 'name', 'follow']
    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELD
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELD


admin.site.register(TwitterUser, CustomUserAdmin)
