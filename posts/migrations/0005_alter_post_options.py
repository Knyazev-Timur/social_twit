# Generated by Django 4.2.3 on 2023-08-17 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
