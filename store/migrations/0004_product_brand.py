# Generated by Django 3.1.3 on 2020-11-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_audio_computer_laptop_smartwatch_tablet_tv'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='brand', max_length=150, verbose_name='Бренд'),
            preserve_default=False,
        ),
    ]
