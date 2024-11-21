from django.core.management.base import BaseCommand
from seminarapp_2_1.models import CoinFlip
import random


class Command(BaseCommand):
    help = "Simulate a coin flip."

    def handle(self, *args, **kwargs):
        flip = CoinFlip(result=random.choice(['heads', 'tails']))
        flip.save()
