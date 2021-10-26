# Generated by Django 3.2.8 on 2021-10-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='images/default_profile_pic.png', upload_to='profile_pic/%Y/%m/%d/'),
        ),
    ]