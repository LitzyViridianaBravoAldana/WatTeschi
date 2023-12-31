# Generated by Django 3.2.4 on 2023-12-07 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('Id_Autor', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=25)),
                ('Apellido_P', models.CharField(max_length=20)),
                ('Apellido_M', models.CharField(max_length=20)),
                ('Biografia', models.TextField()),
            ],
            options={
                'db_table': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('Id_Editorial', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_Editorial', models.TextField()),
                ('Sitio_Web', models.URLField()),
            ],
            options={
                'db_table': 'Editoriales',
            },
        ),
        migrations.CreateModel(
            name='encuestaSatisfaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_encuesta', models.TextField(db_column='id_encuesta')),
                ('correo', models.TextField(db_column='Dirección de correo electrónico')),
                ('pregunta1', models.TextField(db_column='¿Qué tipo de paleta de colores prefieres para el diseño del sistema web de la biblioteca?')),
                ('pregunta2', models.TextField(db_column='¿Qué opinas sobre la personalización de tu perfil en el sistema web de la biblioteca?')),
                ('pregunta3', models.TextField(db_column='¿Cómo te gustaría que se presenten los resultados de búsqueda en el sistema web de la biblioteca?')),
                ('pregunta4', models.TextField(db_column='¿Cuál de las siguientes opciones de búsqueda preferirías en el sistema web de la biblioteca?')),
                ('pregunta5', models.TextField(db_column='¿Qué función consideras más importante para un acceso rápido en la página principal del sistema web de la biblioteca?')),
                ('pregunta6', models.TextField(db_column='¿Dónde preferirías ver las notificaciones en el sistema web de la biblioteca?')),
                ('pregunta7', models.TextField(db_column='¿Te gustaría poder personalizar las notificaciones que recibes en el sistema web de la biblioteca?')),
            ],
            options={
                'db_table': 'encuestaSatisfaccion',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('Id_Categoria', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.TextField()),
            ],
            options={
                'db_table': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('Id_Idioma', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=25, unique=True)),
                ('Codigo_Idioma', models.TextField()),
            ],
            options={
                'db_table': 'Idiomas',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('Id_Libro', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha_Registro', models.DateField()),
                ('Titulo', models.TextField()),
                ('Sinopsis', models.CharField(max_length=300)),
                ('en_biblioteca', models.BooleanField(default=True)),
                ('Fk_Id_Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.autor')),
                ('Fk_Id_Editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.editorial')),
                ('Fk_Id_Genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.genero')),
                ('Fk_Id_Idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.idioma')),
            ],
            options={
                'db_table': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('Id_Pais', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.TextField()),
                ('Codigo_Pais', models.TextField()),
            ],
            options={
                'db_table': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Id_Usuario', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_Usuario', models.TextField()),
                ('Contrasena', models.TextField()),
                ('Nombre', models.TextField()),
                ('Apellido_P', models.CharField(max_length=20)),
                ('Correo', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('Id_Resena', models.AutoField(primary_key=True, serialize=False)),
                ('Calificacion', models.IntegerField()),
                ('Comentario', models.CharField(max_length=150)),
                ('Fk_Id_Libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.libro')),
                ('Fk_Id_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
            options={
                'db_table': 'Resena',
            },
        ),
        migrations.CreateModel(
            name='Libro_has_Idioma',
            fields=[
                ('Id_Libro_has_Idioma', models.AutoField(primary_key=True, serialize=False)),
                ('Fk_Id_Idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.idioma')),
                ('Fk_Id_Libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.libro')),
            ],
            options={
                'db_table': 'Libro_has_Idioma',
            },
        ),
        migrations.CreateModel(
            name='Libro_has_Genero',
            fields=[
                ('Id_Libro_has_Genero', models.AutoField(primary_key=True, serialize=False)),
                ('Fk_Id_Genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.genero')),
                ('Fk_Id_Libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.libro')),
            ],
            options={
                'db_table': 'Libro_has_Genero',
            },
        ),
        migrations.CreateModel(
            name='Libro_has_Autor',
            fields=[
                ('Id_Libro_has_Autor', models.AutoField(primary_key=True, serialize=False)),
                ('Fk_Id_Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.autor')),
                ('Fk_Id_Libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.libro')),
            ],
            options={
                'db_table': 'Libro_has_Autor',
            },
        ),
        migrations.AddField(
            model_name='editorial',
            name='Fk_Id_Pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pais'),
        ),
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('Id_Biblioteca', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha_Inicio', models.DateTimeField()),
                ('Fk_Id_Libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.libro')),
                ('Fk_Id_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
            options={
                'db_table': 'Biblioteca',
            },
        ),
        migrations.AddField(
            model_name='autor',
            name='Fk_Id_Pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pais'),
        ),
    ]
