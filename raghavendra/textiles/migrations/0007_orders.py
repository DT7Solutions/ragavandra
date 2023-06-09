# Generated by Django 4.1.2 on 2023-04-25 06:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textiles', '0006_alter_registerusers_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('OrderID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('WhatsappNo', models.IntegerField(blank=True, max_length=10, null=True)),
                ('ContactNo', models.IntegerField(blank=True, max_length=10, null=True)),
                ('Address', models.CharField(max_length=250)),
                ('street_name', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('Courier', models.CharField(max_length=30)),
                ('TrackingId', models.CharField(blank=True, default=0, max_length=10, null=True)),
                ('No_Of_Items', models.IntegerField(blank=True, max_length=10, null=True)),
                ('file', models.FileField(upload_to='media/')),
                ('OrderStatus', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('Date', models.DateTimeField(default=datetime.datetime(2023, 4, 25, 11, 48, 35, 683506))),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='textiles.registerusers')),
            ],
        ),
    ]
