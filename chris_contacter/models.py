from django.contrib import admin
from django.db import models

PRIORITIES = (
    (10, 'Chat'),
    (20, 'Email'),
    (30, 'Text'),
    (40, 'Call'),
)


class Conversation(models.Model):
    created = models.DateTimeField(auto_created=True)
    message = models.TextField()
    priority = models.PositiveIntegerField(choices=PRIORITIES)
    responded = models.BooleanField(default=False)


admin.site.register(Conversation)
