# Generated by Django 2.1.15 on 2020-09-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novosti', '0020_postimagethumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='redni',
        ),
        migrations.AddField(
            model_name='post',
            name='pozadinskaSlika',
            field=models.CharField(default='var(--clr-green)', max_length=20),
        ),
    ]
