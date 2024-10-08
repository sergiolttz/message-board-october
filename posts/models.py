from django.db import models

# Create your models here.
class Publication(models.Model):
    text = models.TextField(default="")

    def __str__(self) -> str:
        return self.text[:50]