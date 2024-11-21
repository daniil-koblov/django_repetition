from django.db import models

# Create your models here.


class CoinFlip(models.Model):
    FLIP_CHOICES = [('H', 'Heads'), ('T', 'Tails')]

    result = models.CharField(max_length=1, choices=FLIP_CHOICES)
    flip_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.result} flipped at {self.flip_time}'
