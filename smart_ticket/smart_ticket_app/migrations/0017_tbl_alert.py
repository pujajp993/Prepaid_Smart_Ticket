# Generated by Django 5.0.3 on 2024-04-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_ticket_app', '0016_tbl_smartcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=25, verbose_name='Email')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('message', models.CharField(max_length=25, verbose_name='Message')),
            ],
        ),
    ]
