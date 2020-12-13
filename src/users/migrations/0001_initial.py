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
            name='Usuario',
            fields=[
                ('idusuario', models.CharField(db_column='IDUsuario', max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(db_column='Contrase�a', max_length=50)),
                ('tipo_usuario', models.CharField(db_column='Tipo_Usuario', max_length=22)),
                ('pregunta1', models.CharField(db_column='Pregunta1', max_length=45)),
                ('pregunta2', models.CharField(db_column='Pregunta2', max_length=45)),
                ('respuesta1', models.CharField(db_column='Respuesta1', max_length=45)),
                ('respuesta2', models.CharField(db_column='Respuesta2', max_length=45)),
                ('ci_related', models.OneToOneField(db_column='CI', on_delete=django.db.models.deletion.CASCADE, to='persona.Persona')),
            ],
            options={
                'db_table': 'usuario',
                'managed': True,
            },
            bases=('persona.persona',),
        ),
    ]
