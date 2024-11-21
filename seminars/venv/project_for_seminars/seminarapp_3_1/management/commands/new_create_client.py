from django.core.management.base import BaseCommand
from seminarapp_3_1.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        for i in range(1, 5):
            client = Client(
                name=f"Client {i}",
                email=f"example{i}@mail.com",
                phone=f"+7({i}{i}{i})-222-33-33",
                address="Spb",
            )
            client.save()
        self.stdout.write(self.style.SUCCESS(f"Client:'{client}' is registered"))
