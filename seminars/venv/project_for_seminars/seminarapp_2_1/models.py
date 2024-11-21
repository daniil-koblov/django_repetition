from django.db import models

# Create your models here.


class CoinFlip(models.Model):
    RESULT_CHOICES = [('heads', 'Орел'), ('tails', 'Решка')]

    result = models.CharField(max_length=5, choices=RESULT_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_n_flips_stats(n):
        flips = CoinFlip.objects.order_by('-timestamp')[:n]
        stats = {'heads': 0, 'tails': 0}
        for flip in flips:
            if flip.result == 'heads':
                stats['heads'] += 1
            else:
                stats['tails'] += 1
        return stats

    def __str__(self):
        return f'{self.result} flipped at {self.timestamp}'


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f'{self.name} {self.last_name}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)


