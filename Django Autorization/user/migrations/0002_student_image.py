# Generated by Django 4.0.1 on 2022-09-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='', upload_to='user/images'),
        ),
    ]
