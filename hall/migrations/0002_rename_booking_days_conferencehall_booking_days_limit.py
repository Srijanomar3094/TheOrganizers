# Generated by Django 4.2.7 on 2023-11-21 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conferencehall',
            old_name='booking_days',
            new_name='booking_days_limit',
        ),
    ]