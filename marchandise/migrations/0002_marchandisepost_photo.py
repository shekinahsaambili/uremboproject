# Generated by Django 5.0.3 on 2024-04-17 10:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marchandise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marchandisepost',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/'),
            preserve_default=False,
        ),
    ]
