# Generated by Django 3.2 on 2022-10-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='localPhone',
            field=models.CharField(max_length=11, verbose_name='Número de teléfono'),
        ),
    ]