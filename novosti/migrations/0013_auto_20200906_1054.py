# Generated by Django 2.1.15 on 2020-09-06 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novosti', '0012_auto_20200906_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, default='images/default.jpg', upload_to='images/'),
        ),
    ]