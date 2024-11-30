from django.contrib import admin

# Register your models here.
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'created_date')
    list_filter = ('completed', 'created_date')
    search_fields = ('title', 'description')