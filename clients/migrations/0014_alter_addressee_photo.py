# Generated by Django 3.2 on 2022-10-18 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_alter_addressee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressee',
            name='photo',
            field=models.ImageField(default=1, upload_to='', verbose_name='Foto'),
            preserve_default=False,
        ),
    ]
