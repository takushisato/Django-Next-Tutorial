# Generated by Django 4.0.6 on 2022-12-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_iamge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='iamge',
            field=models.ImageField(blank=True, default='images/mystery-man.png', null=True, upload_to='images', verbose_name='プロフィール画像'),
        ),
    ]
