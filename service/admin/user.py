from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin

from service.models import *


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (None, {'fields': ('username', 'nickname', 'position', 'profile_image', 'phone_number')}),

    list_display = ('username', 'nickname', 'position')
    search_fields = ('username', 'nickname', 'position')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status', )
    search_fields = ('title', 'status')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('city', 'name',)
    search_fields = ('city', 'name')
