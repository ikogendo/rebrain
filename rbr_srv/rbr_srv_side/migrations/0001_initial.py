# Generated by Django 4.2.11 on 2024-12-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('ip_address', models.GenericIPAddressField(default='0.0.0.0', verbose_name='IP')),
                ('description', models.TextField(default='no_description', max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Server',
                'managed': True,
            },
        ),
    ]
