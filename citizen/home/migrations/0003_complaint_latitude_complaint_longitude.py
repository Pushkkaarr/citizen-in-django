# Generated by Django 5.0.3 on 2024-04-01 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='complaint',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]
