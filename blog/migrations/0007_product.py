# Generated by Django 5.0.3 on 2024-05-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=100)),
                ('photos', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('prix', models.IntegerField(default=0)),
                ('origine', models.CharField(max_length=100)),
            ],
        ),
    ]
