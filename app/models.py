from django.db import models

# Create your models here.
class ShortURL(models.Model):
    short_url = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.short_url

class LongURL(models.Model):
    short_url = models.ForeignKey(ShortURL, on_delete=models.CASCADE)
    long_url = models.URLField(max_length=500)

    def __str__(self):
        return self.long_url