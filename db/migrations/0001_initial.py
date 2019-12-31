# Generated by Django 3.0 on 2019-12-30 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('mail', models.EmailField(max_length=254)),
                ('icon', models.ImageField(height_field=100, upload_to='', width_field=100)),
                ('friends', models.ManyToManyField(related_name='_user_friends_+', to='db.User')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(height_field=500, upload_to='', width_field=500)),
                ('likes', models.ManyToManyField(related_name='likes', to='db.User')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='db.User')),
            ],
        ),
    ]