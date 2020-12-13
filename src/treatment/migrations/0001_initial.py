# Generated by Django 2.2.2 on 2019-12-26 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('cod_tratamiento', models.AutoField(db_column='Cod_Tratamiento', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(db_column='Descripcion')),
                ('frecuencia', models.CharField(db_column='Frecuencia', max_length=7)),
                ('tiempo_necesario', models.CharField(db_column='Tiempo_Necesario', max_length=20)),
                ('num_serv_necesario', models.IntegerField(db_column='Num_Serv_Necesario')),
                ('cod_paciente', models.ForeignKey(db_column='Cod_Diagnostico', on_delete=django.db.models.deletion.CASCADE, to='patients.Paciente', unique=True)),
            ],
            options={
                'db_table': 'tratamiento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('cod_servicio', models.AutoField(db_column='Cod_Servicio', primary_key=True, serialize=False)),
                ('precio', models.FloatField(db_column='Precio')),
                ('tipo1', models.CharField(db_column='Tipo1', max_length=20)),
                ('tipo2', models.CharField(blank=True, db_column='Tipo2', max_length=20, null=True)),
                ('tipo3', models.CharField(blank=True, db_column='Tipo3', max_length=20, null=True)),
                ('cod_cita', models.ForeignKey(db_column='Cod_Cita', on_delete=django.db.models.deletion.CASCADE, to='appointments.Citas', unique=True)),
            ],
            options={
                'db_table': 'servicio',
                'managed': True,
            },
        ),
    ]
