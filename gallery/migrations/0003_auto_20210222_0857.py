# Generated by Django 3.1.6 on 2021-02-22 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20210222_0830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='img_cat',
            new_name='post_cat',
        ),
    ]
