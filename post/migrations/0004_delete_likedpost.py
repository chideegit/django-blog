# Generated by Django 5.0 on 2023-12-14 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_likedpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LikedPost',
        ),
    ]
