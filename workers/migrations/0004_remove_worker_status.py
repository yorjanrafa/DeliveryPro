# Generated by Django 3.2 on 2022-10-13 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_rename_lastname_worker_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='status',
        ),
    ]
