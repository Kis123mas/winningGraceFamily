# Generated by Django 4.2.2 on 2023-06-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_newuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile2.png', null=True, upload_to=''),
        ),
    ]
