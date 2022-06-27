from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("name",)}

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity')
    list_display_links = ('id', 'activity')
    search_fields = ('activity',)
    prepopulated_fields = {"slug": ("activity",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Role, RoleAdmin)

