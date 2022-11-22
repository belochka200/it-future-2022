from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название статьи")
    content = models.TextField(verbose_name="Текст статьи")

    def __str__(self):
        return self.title

    