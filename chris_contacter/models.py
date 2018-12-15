from django.contrib import admin
from django.db import models

PRIORITIES = (
    (0, 'Unsent'),
    (10, 'Chat'),
    (20, 'Email'),
    (30, 'Text'),
    (40, 'Call'),
)


class Conversation(models.Model):
    message = models.TextField()
    priority = models.PositiveIntegerField(choices=PRIORITIES, help_text='Highest medium to try')
    status = models.PositiveIntegerField(choices=PRIORITIES, default=0, help_text='Highest medium tried')
    sent = models.DateTimeField(blank=True, null=True)
    responded = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.get_priority_display()}: {self.message[:50]}'


admin.site.register(Conversation)
