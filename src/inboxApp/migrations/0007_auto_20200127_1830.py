# Generated by Django 3.0.2 on 2020-01-28 02:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inboxApp', '0006_auto_20200127_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessages',
            name='created_date',
        ),
        migrations.AddField(
            model_name='usermessages',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 2, 30, 17, 258529, tzinfo=utc)),
        ),
    ]
