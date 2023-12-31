# Generated by Django 3.2.4 on 2024-01-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_biblioteca_libro_libro_has_autor_libro_has_genero_libro_has_idioma_resena'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro_has_autor',
            name='Fk_Id_Autor',
        ),
        migrations.RemoveField(
            model_name='libro_has_autor',
            name='Fk_Id_Libro',
        ),
        migrations.RemoveField(
            model_name='libro_has_genero',
            name='Fk_Id_Genero',
        ),
        migrations.RemoveField(
            model_name='libro_has_genero',
            name='Fk_Id_Libro',
        ),
        migrations.RemoveField(
            model_name='libro_has_idioma',
            name='Fk_Id_Idioma',
        ),
        migrations.RemoveField(
            model_name='libro_has_idioma',
            name='Fk_Id_Libro',
        ),
        migrations.RemoveField(
            model_name='resena',
            name='Fk_Id_Libro',
        ),
        migrations.RemoveField(
            model_name='resena',
            name='Fk_Id_Usuario',
        ),
        migrations.AddField(
            model_name='libro',
            name='Archivo',
            field=models.FileField(blank=True, null=True, upload_to='files/libros/'),
        ),
        migrations.AddField(
            model_name='libro',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/libros/'),
        ),
        migrations.DeleteModel(
            name='Biblioteca',
        ),
        migrations.DeleteModel(
            name='Libro_has_Autor',
        ),
        migrations.DeleteModel(
            name='Libro_has_Genero',
        ),
        migrations.DeleteModel(
            name='Libro_has_Idioma',
        ),
        migrations.DeleteModel(
            name='Resena',
        ),
    ]
