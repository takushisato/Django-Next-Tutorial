# Generated by Django 4.0.6 on 2022-12-19 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_iamge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='iamge',
            new_name='image',
        ),
    ]
