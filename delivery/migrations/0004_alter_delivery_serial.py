# Generated by Django 3.2 on 2022-12-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_alter_delivery_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='serial',
            field=models.CharField(default='@m&t~fsC#9[]|7F0vTnI½hyº=¬wpWR?HQo1cZK)(S%!2d4·igb8q6GkuDVMN', max_length=70, unique=True),
        ),
    ]