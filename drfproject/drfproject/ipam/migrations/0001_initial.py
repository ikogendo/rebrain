# Generated by Django 5.1.1 on 2024-09-13 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='CY-', max_length=10)),
                ('city', models.CharField(max_length=64)),
                ('floor', models.IntegerField(default='0')),
                ('street', models.CharField(default='Makariou', max_length=128)),
                ('build_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('user', models.CharField(max_length=64)),
                ('date_startuse', models.DateTimeField(default='2000-01-01 00:00:00')),
                ('date_lastuse', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField(default='192.168.0.1')),
                ('type_address', models.CharField(default='DHCP', max_length=6)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ipam.build')),
            ],
        ),
    ]
