from django.core.management.base import BaseCommand
from seminarapp_2_1.models import Author


class Command(BaseCommand):
    help = "Create author."

    def handle(self, *args, **kwargs):
        author = Author(
            name='Данил',
            last_name='Иванов',
            email='danil@example.com',
            bio='Более менее знаю Python и Django.',
            birthday='1990-01-01'
        )
        author.save()
        self.stdout.write(f'Автор: {author.full_name} добавлен в базу.')
