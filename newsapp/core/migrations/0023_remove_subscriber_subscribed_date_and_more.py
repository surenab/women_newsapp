# Generated by Django 4.2.2 on 2023-09-14 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_subscriber_delete_subscribedusers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='subscribed_date',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='subscribed_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
