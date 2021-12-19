# Generated by Django 3.2.9 on 2021-12-19 13:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0005_alter_activity_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='participants',
            field=models.ManyToManyField(related_name='re_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
