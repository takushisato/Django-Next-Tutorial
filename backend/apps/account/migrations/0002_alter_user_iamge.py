# Generated by Django 4.0.6 on 2022-12-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='iamge',
            field=models.ImageField(blank=True, default='profile/mystery-man.png', null=True, upload_to='images', verbose_name='プロフィール画像'),
        ),
    ]