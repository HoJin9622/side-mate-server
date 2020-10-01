from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin

from service.models import *


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        # (None, {'fields': ('nickname', 'phone_number')}),
        (None, {'fields': ('nickname', )}),
    )
    list_display = ('username', 'nickname',)
    search_fields = ('username', 'nickname',)

    # list_display = ('nickname', 'phone_number', 'email')
    # search_fields = ('nickname', 'phone_number', 'email')
