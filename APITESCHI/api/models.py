from django.db import models

# Create your models here.
class Usuario(models.Model):
    Id_Usuario = models.AutoField(primary_key=True)
    Nombre_Usuario = models.TextField()
    Contrasena = models.TextField()
    Nombre = models.TextField()
    Apellido_Pa = models.CharField(max_length=20)
    Correo = models.EmailField(unique=True)

    class Meta:
        db_table = 'Usuarios'

class Genero(models.Model):
    Id_Categoria = models.AutoField(primary_key=True)
    Descripcion = models.TextField()
    
    class Meta:
        db_table = 'Generos'

class Pais(models.Model):
    Id_Pais = models.AutoField(primary_key=True)
    Descripcion = models.TextField()
    Codigo_Pais = models.TextField()

    class Meta:
        db_table = 'Paises'

class Idioma(models.Model):
    Id_Idioma = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=25, unique=True)
    Codigo_Idioma = models.TextField()

    class Meta:
        db_table = 'Idiomas'

class Editorial(models.Model):
    Id_Editorial = models.AutoField(primary_key=True)
    Fk_Id_Pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    Nombre_Editorial = models.TextField()
    Sitio_Web = models.URLField()

    class Meta:
        db_table = 'Editoriales'


class Autor(models.Model):
    Id_Autor = models.AutoField(primary_key=True)
    Fk_Id_Pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=25)
    Apellido_P = models.CharField(max_length=20)
    Apellido_M = models.CharField(max_length=20)
    Biografia = models.TextField()
    # Estructura de la carpeta para las imágenes
    Imagen = models.ImageField(upload_to='images/autores/', null=True, blank=True)
    class Meta:
        db_table='Autores'

class Libro(models.Model):
    Id_Libro = models.AutoField(primary_key=True)
    Fk_Id_Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    Fk_Id_Genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    Fk_Id_Editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    Fk_Id_Idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    Fecha_Registro = models.DateField()
    Titulo = models.TextField()
    Sinopsis = models.CharField(max_length=300)
    en_biblioteca = models.BooleanField(default=True)
    # Estructura de la carpeta para las imágenes
    Imagen = models.ImageField(upload_to='images/libros/', null=True, blank=True)
    # Estructura de la carpeta para los archivos
    Archivo = models.FileField(upload_to='files/libros/', null=True, blank=True)

    class Meta:
        db_table = 'Libros'
        
class Resena(models.Model):
    Id_Resena = models.AutoField(primary_key=True)
    Fk_Id_Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    Fk_Id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Calificacion = models.IntegerField()
    Comentario = models.CharField(max_length=150)

    class Meta:
        db_table = 'Resena'

class Biblioteca(models.Model):
    Id_Biblioteca = models.AutoField(primary_key=True)
    Fk_Id_Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    Fk_Id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Fecha_Inicio = models.DateTimeField()

    class Meta:
        db_table = 'Biblioteca'

class Libro_has_Autor(models.Model):
    Id_Libro_has_Autor = models.AutoField(primary_key=True)
    Fk_Id_Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    Fk_Id_Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Libro_has_Autor'

class Libro_has_Idioma(models.Model):
    Id_Libro_has_Idioma = models.AutoField(primary_key=True)
    Fk_Id_Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    Fk_Id_Idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Libro_has_Idioma'


class Libro_has_Genero(models.Model):
    Id_Libro_has_Genero = models.AutoField(primary_key=True)
    Fk_Id_Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    Fk_Id_Genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Libro_has_Genero'

class encuestaSatisfaccion(models.Model):
    id_encuesta = models.TextField(db_column='id_encuesta')
    correo = models.TextField(db_column='Dirección de correo electrónico')
    pregunta1 = models.TextField(db_column='¿Qué tipo de paleta de colores prefieres para el diseño del sistema web de la biblioteca?')
    pregunta2 = models.TextField(db_column='¿Qué opinas sobre la personalización de tu perfil en el sistema web de la biblioteca?')
    pregunta3 = models.TextField(db_column='¿Cómo te gustaría que se presenten los resultados de búsqueda en el sistema web de la biblioteca?')
    pregunta4 = models.TextField(db_column='¿Cuál de las siguientes opciones de búsqueda preferirías en el sistema web de la biblioteca?')
    pregunta5 = models.TextField(db_column='¿Qué función consideras más importante para un acceso rápido en la página principal del sistema web de la biblioteca?')
    pregunta6 = models.TextField(db_column='¿Dónde preferirías ver las notificaciones en el sistema web de la biblioteca?')
    pregunta7 = models.TextField(db_column='¿Te gustaría poder personalizar las notificaciones que recibes en el sistema web de la biblioteca?')
    class Meta:
        db_table = 'encuestaSatisfaccion'