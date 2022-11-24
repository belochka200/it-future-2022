# Generated by Django 4.1.3 on 2022-11-24 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Категория',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('название', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название статьи')),
                ('content', models.TextField(verbose_name='Текст статьи')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='лайки')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='просмотры')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.категория')),
            ],
        ),
    ]
