# Generated by Django 4.2.3 on 2023-08-15 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bithday',
            new_name='birthday',
        ),
    ]
