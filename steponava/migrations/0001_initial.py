# Generated by Django 4.2.2 on 2023-08-13 22:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Įveskite medžiojimo būdą (pvz. tykojant)', max_length=10, verbose_name='Medžiojimo būdas')),
            ],
        ),
        migrations.CreateModel(
            name='Lapas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeris', models.CharField(max_length=10, verbose_name='Numeris')),
                ('zverys', models.TextField(help_text='Leidžiami medžioti žvėrys', max_length=200, verbose_name='Aprašymas')),
                ('budas', models.ForeignKey(help_text='Parinkite medžiojimo būdą šiam medžioklės lapui', null=True, on_delete=django.db.models.deletion.SET_NULL, to='steponava.budas')),
            ],
        ),
        migrations.CreateModel(
            name='Vadovas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Vardas')),
                ('last_name', models.CharField(max_length=100, verbose_name='Pavardė')),
                ('bilietas', models.CharField(max_length=10, verbose_name='Medžiotojo bilieto numeris')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='LapasInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unikalus ID', primary_key=True, serialize=False)),
                ('issued', models.DateField(blank=True, null=True, verbose_name='Išduotas')),
                ('due_valid', models.DateField(blank=True, null=True, verbose_name='Galioja iki')),
                ('status', models.CharField(blank=True, choices=[('n', 'Naujas'), ('i', 'Išduotas'), ('p', 'Panaudotas')], default='n', help_text='Statusas', max_length=1)),
                ('lapas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='steponava.lapas')),
            ],
        ),
        migrations.AddField(
            model_name='lapas',
            name='vadovas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='steponava.vadovas'),
        ),
    ]