from django.db import models

# Create your models here.

class CoinFlip(models.Model):
    HEADS = 'H'
    TAILS = 'T'
    FLIP_CHOICES = [(HEADS, 'Heads'), (TAILS, 'Tails')]

    result = models.CharField(max_length=1, choices=FLIP_CHOICES)
    flip_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Flip result: {self.get_result_display()}, Flip time: {self.flip_time}'