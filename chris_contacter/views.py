from django.views.generic import CreateView

from .models import Conversation


class ConversationCreateView(CreateView):
    model = Conversation
    fields = ('message', 'priority')
