from django.contrib import admin
from django.db import models

PRIORITY_CHOICES = (
    (0, 'Unsent'),
    (10, 'Chat'),
    (20, 'Email'),
    (30, 'Text'),
    (40, 'Call'),
)
PRIORITIES = (priority[0] for priority in PRIORITY_CHOICES)


class Conversation(models.Model):
    message = models.TextField()
    priority = models.PositiveIntegerField(choices=PRIORITY_CHOICES, help_text='Highest medium to try')
    status = models.PositiveIntegerField(choices=PRIORITY_CHOICES, default=0, help_text='Highest medium tried')
    sent = models.DateTimeField(blank=True, null=True)
    responded = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-sent',)

    def __str__(self):
        return f'{self.get_status_display()}: {self.message[:50]}'


admin.site.register(Conversation)
