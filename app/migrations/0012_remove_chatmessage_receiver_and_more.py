# Generated by Django 4.2.1 on 2023-09-09 13:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_chatmessage_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='sender',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='receiver_username',
            field=models.CharField(default='system', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='sender_username',
            field=models.CharField(default='system', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]