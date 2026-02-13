from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    fieldsets = [
        (None,              {'fields': ['name', 'slug']}),
        ('Social Features', {'fields': ['views', 'likes']})
    ]
    list_display = ('name', 'views', 'likes')

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Information', {'fields': ['category', 'url']}),
        ('Social Features', {'fields': ['views']})
    ]
    list_display = ('title', 'category', 'url')
    list_filter = ['category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin) # category, title, url, views