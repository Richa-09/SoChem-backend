# Generated by Django 3.1.2 on 2020-10-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20201012_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
