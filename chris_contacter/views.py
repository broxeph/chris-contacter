from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Conversation


class ConversationCreateView(CreateView):
    model = Conversation
    fields = ('message', 'priority')
    success_url = reverse_lazy('conversation-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Send!', css_class='btn-primary'))
        return form


class ConversationListView(ListView):
    model = Conversation
