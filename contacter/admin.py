from django.contrib import admin

from contacter.models import Conversation


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'priority', 'status', 'sent', 'responded', 'message')
admin.site.register(Conversation, ConversationAdmin)
