# Generated by Django 4.2.7 on 2023-11-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0003_alter_booking_ao_approval_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ao_status_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='hod_status_date',
            field=models.DateTimeField(null=True),
        ),
    ]
