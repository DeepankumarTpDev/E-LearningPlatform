from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'content', 'timestamp', 'course']
    list_filter = ['course', 'timestamp', 'sender']
    search_fields = ['sender', 'course']
