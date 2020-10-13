# Generated by Django 3.1.2 on 2020-10-12 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20201012_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumpost',
            old_name='date_time',
            new_name='date',
        ),
        migrations.AddField(
            model_name='forumpost',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
