# Generated by Django 4.1.2 on 2023-06-07 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textiles', '0012_alter_orders_date_alter_orders_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='item_color',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='item_size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 16, 3, 13, 375258)),
        ),
    ]
