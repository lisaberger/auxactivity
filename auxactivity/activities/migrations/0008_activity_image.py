# Generated by Django 3.2.9 on 2021-12-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_alter_activity_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(default='activity_default_placeholder.png', upload_to='activities', verbose_name='Activities'),
        ),
    ]
