# Generated by Django 2.1.5 on 2020-06-17 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
        ('prestadores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='especialidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='prestadores.Especialidade', verbose_name='Especialidade'),
        ),
        migrations.AddField(
            model_name='medicamentos',
            name='nm_medicamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacientes.Farm_medicamentos'),
        ),
        migrations.AddField(
            model_name='medicamentos',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacientes.DadosPaciente'),
        ),
    ]
