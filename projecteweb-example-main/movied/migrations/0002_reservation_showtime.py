# Generated by Django 5.0.4 on 2024-05-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movied', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='showtime',
            field=models.IntegerField(default=None),
        ),
    ]
