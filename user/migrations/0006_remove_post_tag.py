# Generated by Django 4.2 on 2023-04-12 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
    ]