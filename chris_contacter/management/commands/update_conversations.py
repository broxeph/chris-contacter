from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Sends messages and updates conversation statuses'

    def handle(self, *args, **options):
        print('yay!')
