# Generated by Django 3.0.2 on 2020-01-28 02:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inboxApp', '0005_usermessages_conversation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessages',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 1, 28, 2, 22, 18, 836198, tzinfo=utc)),
        ),
    ]
