# Generated by Django 4.1.2 on 2023-05-04 06:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('textiles', '0008_remove_orders_userid_alter_orders_contactno_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegisterUsers',
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 23, 2, 25, 377505)),
        ),
    ]
