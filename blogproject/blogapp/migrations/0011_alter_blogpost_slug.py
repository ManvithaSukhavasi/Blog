# Generated by Django 4.0 on 2022-02-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_rename_image_blogpost_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(max_length=130),
        ),
    ]