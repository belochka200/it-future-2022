from django.db import models


class Категория(models.Model):
    название = models.CharField(max_length=255)

    def __str__(self):
        return self.название


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название статьи")
    content = models.TextField(verbose_name="Текст статьи")
    likes = models.PositiveIntegerField(verbose_name="лайки", default=0)
    views = models.PositiveIntegerField(verbose_name="просмотры", default=0)
    category = models.ForeignKey(Категория, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title   