# Generated by Django 4.2.3 on 2023-08-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(null=True, to='comments.comment', verbose_name='Комментарии'),
        ),
    ]