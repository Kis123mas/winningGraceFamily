# Generated by Django 4.2.2 on 2023-06-15 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdash', '0002_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Announcement',
        ),
    ]
