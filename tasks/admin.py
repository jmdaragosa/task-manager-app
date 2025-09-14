from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'deadline', 'completed')
    list_filter = ('completed', 'deadline')
    search_fields = ('title', 'owner__username')
