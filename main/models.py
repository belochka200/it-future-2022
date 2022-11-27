from django.db import models
from django.contrib.auth.models import User


class Категория(models.Model):
    название = models.CharField(max_length=255)

    def __str__(self):
        return self.название

# Create your models here.
class Post(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(pk=1))
    title = models.CharField(max_length=255, verbose_name="Название статьи")
    content = models.TextField(verbose_name="Текст статьи")
    likes = models.PositiveIntegerField(verbose_name="лайки", default=0)
    views = models.PositiveIntegerField(verbose_name="просмотры", default=0)
    category = models.ForeignKey(Категория, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return '/post/{}'.format(self.pk)

    def __str__(self):
        return self.title   