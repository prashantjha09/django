# Generated by Django 2.1.3 on 2018-11-04 15:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_Posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 4, 15, 39, 38, 42159, tzinfo=utc)),
        ),
    ]