# Generated by Django 3.2.9 on 2021-11-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='alumno',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='fechafin',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='fechainicio',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
