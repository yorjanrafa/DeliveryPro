# Generated by Django 3.2 on 2022-10-22 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_payment_centralist'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='google_map',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion de google map'),
        ),
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='addressee',
            name='google_map',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion de google map'),
        ),
        migrations.AlterField(
            model_name='addressee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
    ]
