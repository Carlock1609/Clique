# Generated by Django 3.0.2 on 2020-01-23 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0023_auto_20200121_1640'),
        ('inboxApp', '0002_delete_conversationdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='inboxdb',
            name='profile_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
        migrations.CreateModel(
            name='ConversationDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Inbox',
            },
        ),
    ]
