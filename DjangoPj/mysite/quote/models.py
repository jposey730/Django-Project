from django.db import models

class Day(models.Model):
    date = models.DateTimeField()
    author = models.CharField(max_length=45)
    quote = models.TextField()

    def __str__(self):
        return str(self.date)

