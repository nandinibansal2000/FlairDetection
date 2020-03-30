from django.db import models

class Data(models.Model):
    link = models.CharField(blank = False, max_length = 300)

    def __str__(self):
        return self.link
