# Generated by Django 3.1.5 on 2021-01-20 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='profiles/images', verbose_name='Personal Image'),
        ),
    ]
