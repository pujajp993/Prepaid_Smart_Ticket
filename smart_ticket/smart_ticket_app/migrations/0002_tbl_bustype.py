# Generated by Django 5.0.3 on 2024-03-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_ticket_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_bustype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bus_type', models.CharField(max_length=25)),
            ],
        ),
    ]
