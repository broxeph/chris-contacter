from django.contrib import admin
from django.db import models

UNSENT = 'Unsent'
CHAT = 'Chat'
EMAIL = 'Email'
TEXT = 'Text'
CALL = 'Call'
PRIORITY_CHOICES = (
    (0, UNSENT),
    (10, CHAT),
    (20, EMAIL),
    (30, TEXT),
    (40, CALL),
)


class Conversation(models.Model):
    message = models.TextField()
    priority = models.PositiveIntegerField(choices=PRIORITY_CHOICES, help_text='Highest service to try')
    status = models.PositiveIntegerField(choices=PRIORITY_CHOICES, default=0, help_text='Highest service tried')
    sent = models.DateTimeField(blank=True, null=True)
    responded = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-sent',)

    def __str__(self):
        return f'{self.get_status_display()}: {self.message[:50]}'
