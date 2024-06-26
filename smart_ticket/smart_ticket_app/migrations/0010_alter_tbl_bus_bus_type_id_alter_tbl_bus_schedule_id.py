# Generated by Django 5.0.3 on 2024-03-28 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_ticket_app', '0009_alter_tbl_bus_bus_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_bus',
            name='bus_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_ticket_app.tbl_bustype'),
        ),
        migrations.AlterField(
            model_name='tbl_bus',
            name='schedule_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smart_ticket_app.tbl_schedule'),
        ),
    ]
