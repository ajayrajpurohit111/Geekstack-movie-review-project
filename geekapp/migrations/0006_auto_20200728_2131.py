# Generated by Django 3.0.3 on 2020-07-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekapp', '0005_auto_20200728_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.TextField(max_length=5000),
        ),
        migrations.DeleteModel(
            name='list',
        ),
    ]
