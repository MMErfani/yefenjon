# Generated by Django 4.0.5 on 2022-06-30 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_avatar_user_card_number_user_prof_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='NULL', upload_to='avatars', verbose_name='آواتار'),
        ),
    ]