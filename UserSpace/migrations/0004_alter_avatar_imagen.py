# Generated by Django 4.1 on 2022-09-19 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSpace', '0003_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
