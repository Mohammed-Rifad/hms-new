# Generated by Django 4.1.4 on 2023-01-04 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0005_remove_patient_password'),
        ('hms_admin', '0008_consultation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=10)),
                ('booking_date', models.CharField(max_length=20)),
                ('status', models.CharField(default='booked', max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_admin.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.patient')),
            ],
            options={
                'db_table': 'booking_tb',
            },
        ),
    ]
