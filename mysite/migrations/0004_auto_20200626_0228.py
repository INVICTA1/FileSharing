# Generated by Django 3.0.7 on 2020-06-25 23:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_document_expires_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='expires_doc',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 25, 23, 33, 12, 922325, tzinfo=utc)),
        ),
    ]
