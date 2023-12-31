# Generated by Django 4.2.3 on 2023-08-14 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'director',
                'verbose_name_plural': 'directores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_estreno', models.DateField()),
                ('productora', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'pelicula',
                'verbose_name_plural': 'peliculas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='productoras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'productora',
                'verbose_name_plural': 'productoras',
                'ordering': ['nombre'],
            },
        ),
    ]
