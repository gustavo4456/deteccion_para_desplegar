# Generated by Django 4.2.4 on 2023-10-09 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melanoma_detection_app', '0009_alter_configuracionusuario_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificaciones',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='notificaciones',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
