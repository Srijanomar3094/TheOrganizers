# Generated by Django 4.2.7 on 2023-11-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0002_rename_booking_days_conferencehall_booking_days_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ao_approval_status',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='hod_approval_status',
            field=models.BooleanField(null=True),
        ),
    ]