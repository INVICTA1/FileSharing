# Generated by Django 3.0.7 on 2020-06-25 23:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20200626_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='expires_doc',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 25, 23, 59, 9, 556422, tzinfo=utc)),
        ),
    ]