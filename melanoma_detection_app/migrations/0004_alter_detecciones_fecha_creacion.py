# Generated by Django 4.2.4 on 2023-09-13 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melanoma_detection_app', '0003_alter_detecciones_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detecciones',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
