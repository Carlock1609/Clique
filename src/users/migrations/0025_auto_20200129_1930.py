# Generated by Django 3.0.2 on 2020-01-30 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20200129_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuserpost',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProfileUserPhoto',
        ),
        migrations.DeleteModel(
            name='ProfileUserPost',
        ),
    ]
