# Generated by Django 2.2.2 on 2019-12-26 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cod_paciente', models.AutoField(db_column='Cod_Paciente', primary_key=True, serialize=False)),
                ('diagnostico', models.TextField(db_column='Diagnostico')),
                ('ci_related', models.OneToOneField(db_column='CI', on_delete=django.db.models.deletion.CASCADE, to='persona.Persona')),
            ],
            options={
                'db_table': 'paciente',
                'managed': True,
            },
            bases=('persona.persona',),
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('cod_expediente', models.AutoField(db_column='Cod_Expediente', primary_key=True, serialize=False)),
                ('antecedentes_clinicos', models.TextField(blank=True, db_column='Antecedentes_Clinicos', null=True)),
                ('enfermedades', models.CharField(blank=True, db_column='Enfermedades', max_length=50, null=True)),
                ('alergias', models.CharField(blank=True, db_column='Alergias', max_length=50, null=True)),
                ('cod_paciente', models.OneToOneField(db_column='Cod_Paciente', on_delete=django.db.models.deletion.CASCADE, to='patients.Paciente')),
            ],
            options={
                'db_table': 'expediente',
                'managed': True,
            },
        ),
    ]
