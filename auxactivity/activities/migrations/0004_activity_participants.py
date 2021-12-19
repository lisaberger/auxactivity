# Generated by Django 3.2.9 on 2021-12-19 12:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0003_activity_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='participants',
            field=models.ManyToManyField(related_name='re_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
