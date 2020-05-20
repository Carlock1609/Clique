# Generated by Django 3.0.2 on 2020-01-23 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0023_auto_20200121_1640'),
        ('inboxApp', '0003_auto_20200122_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, default="Let's Collaborate!", max_length=100, null=True)),
                ('body', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('user_inbox', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'User Individual Messages',
            },
        ),
        migrations.RemoveField(
            model_name='inboxdb',
            name='profile_id',
        ),
        migrations.RemoveField(
            model_name='inboxdb',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='inboxdb',
            name='sender',
        ),
        migrations.DeleteModel(
            name='ConversationDB',
        ),
        migrations.DeleteModel(
            name='InboxDB',
        ),
    ]