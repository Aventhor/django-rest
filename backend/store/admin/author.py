from django.contrib import admin

from store.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'middle_name', 'created_at']
