# Generated by Django 4.1.6 on 2023-02-06 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_rating_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='owner',
            field=models.CharField(blank=True, max_length=150, verbose_name='Autor'),
        ),
    ]