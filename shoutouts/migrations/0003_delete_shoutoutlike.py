# Generated by Django 3.0 on 2019-12-09 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoutouts', '0002_shoutoutlike'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShoutoutLike',
        ),
    ]
