# Generated by Django 5.1.1 on 2024-10-25 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='profile_images/default_profileimg.jpg', upload_to='profile_images'),
        ),
    ]
