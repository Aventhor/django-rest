from django.contrib import admin
from store.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    #list_display = ['name', 'email', 'message', 'created_at']
