# Generated by Django 4.1.6 on 2023-02-06 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rating_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='clinte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.client', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='motoTax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.mototaxi', verbose_name='Moto Taxi'),
        ),
    ]
