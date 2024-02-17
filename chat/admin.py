from django.contrib import admin
from .models import ChatConversation, ChatCoversationUser
# Register your models here.

class ChatConversationAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'time', 'sender', 'receiver')
    list_filter = ('user',)

admin.site.register(ChatConversation, ChatConversationAdmin)