# Generated by Django 3.2 on 2022-10-22 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0014_alter_addressee_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='centralist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Centralista'),
        ),
    ]
