# Generated by Django 4.2.1 on 2023-05-28 14:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('publicacion', models.CharField(max_length=200)),
                ('fecha_subida', models.DateField(default=datetime.date.today)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categorias')),
            ],
        ),
    ]
