# Generated by Django 4.2.3 on 2023-08-06 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModels',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('catargory', models.CharField(choices=[('mystry', 'Mystry'), ('Threler', 'Threler'), ('Hamour', 'Hamour'), ('Horror', 'Horror')], max_length=20)),
                ('first_pub', models.DateTimeField(auto_now_add=True)),
                ('last_pub', models.DateTimeField()),
            ],
        ),
    ]
