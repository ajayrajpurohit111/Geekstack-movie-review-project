# Generated by Django 3.0.3 on 2020-07-28 21:54

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geekapp', '0013_auto_20200729_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
