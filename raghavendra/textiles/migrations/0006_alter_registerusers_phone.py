# Generated by Django 4.1.2 on 2023-04-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textiles', '0005_alter_registerusers_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerusers',
            name='Phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
