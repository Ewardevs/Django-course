# Generated by Django 4.2.1 on 2023-05-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_publicaciones_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='publicacion',
            field=models.TextField(max_length=2000),
        ),
    ]