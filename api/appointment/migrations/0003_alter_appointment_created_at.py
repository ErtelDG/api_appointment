# Generated by Django 4.1.7 on 2023-02-23 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 2, 23, 19, 48, 17, 295429), default=datetime.datetime(2023, 2, 23, 19, 48, 17, 295429)),
        ),
    ]