# Generated by Django 3.0 on 2019-12-31 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_auto_20191231_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='SocialNet/static/temp-images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, upload_to='SocialNet/static/temp-images'),
        ),
    ]
