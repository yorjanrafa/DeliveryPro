# Generated by Django 3.2 on 2022-10-23 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0019_alter_client_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(default='', upload_to='', verbose_name='Foto'),
            preserve_default=False,
        ),
    ]
