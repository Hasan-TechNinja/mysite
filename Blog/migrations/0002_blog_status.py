# Generated by Django 5.1.7 on 2025-03-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
