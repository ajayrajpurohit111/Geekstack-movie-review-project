# Generated by Django 3.0.3 on 2020-07-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.URLField(blank=True, default='DEFAULT VALUE'),
        ),
    ]