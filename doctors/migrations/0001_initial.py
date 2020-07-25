# Generated by Django 3.0.7 on 2020-07-24 18:41

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import doctors.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(blank=True, choices=[('A', 'Active'), ('C', 'Cancelled')], max_length=1, null=True)),
                ('active', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name=doctors.models.upload_image_path)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'hospital-alias',
                'verbose_name_plural': 'hospital-aliases',
                'db_table': 'hospital-alias',
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name=doctors.models.upload_image_path)),
                ('condition', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=99, null=True)),
                ('doctor_type', models.CharField(blank=True, choices=[('Paediatrician', 'Paediatrician'), ('Dentist', 'Dentist'), ('Neuro-Surgeon', 'Neuro-Surgeon')], max_length=99, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hospital_alias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.HospitalAlias')),
            ],
            options={
                'verbose_name': 'doctors',
                'verbose_name_plural': 'doctorses',
                'db_table': 'doctors',
            },
        ),
    ]