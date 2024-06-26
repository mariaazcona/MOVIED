# Generated by Django 5.0.6 on 2024-05-17 09:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id_cinema', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id_movie', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=20)),
                ('duration', models.CharField(default='-', max_length=10)),
                ('price', models.CharField(max_length=50)),
                ('overview', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=50)),
                ('poster', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id_reservation', models.AutoField(primary_key=True, serialize=False)),
                ('num_tickets', models.IntegerField(default=None)),
                ('showtime', models.IntegerField(default=None)),
                ('cinema_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='movied.cinema')),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='movied.movie')),
            ],
        ),
    ]
