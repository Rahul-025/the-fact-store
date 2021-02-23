# Generated by Django 3.1.6 on 2021-02-23 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20210222_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=30)),
                ('article_author', models.CharField(max_length=20)),
                ('article_desc', models.TextField()),
                ('article_image', models.ImageField(upload_to='article_images')),
                ('date_posted', models.DateTimeField()),
                ('article_slug', models.SlugField(max_length=100)),
                ('article_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.category')),
            ],
        ),
    ]