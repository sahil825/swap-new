# Generated by Django 3.2.6 on 2021-09-01 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coins', '0002_coin_number_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='end_bid_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 1, 0, 13, 59, 271395)),
            preserve_default=False,
        ),
    ]
