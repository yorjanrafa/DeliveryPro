# Generated by Django 3.2 on 2022-10-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0016_auto_20221022_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(default='111.jpg', upload_to='', verbose_name='Foto'),
            preserve_default=False,
        ),
    ]
