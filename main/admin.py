from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'date']
    list_filter = ['date', 'created_at', 'owner']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'owner__email', 'date']
