# Generated by Django 5.0.1 on 2024-01-10 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Strawberry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authors',
            new_name='author',
        ),
    ]
