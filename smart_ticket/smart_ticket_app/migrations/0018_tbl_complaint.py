# Generated by Django 5.0.3 on 2024-04-15 07:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_ticket_app', '0017_tbl_alert'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.EmailField(max_length=25, verbose_name='Subject')),
                ('description', models.CharField(max_length=25, verbose_name='Description')),
                ('complaint_replay', models.CharField(max_length=25, verbose_name='Complaint_replay')),
                ('status', models.CharField(max_length=15, verbose_name='Status')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
