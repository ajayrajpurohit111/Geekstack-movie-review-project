# Generated by Django 3.0.3 on 2020-07-28 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geekapp', '0010_auto_20200729_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='relase_date',
        ),
    ]