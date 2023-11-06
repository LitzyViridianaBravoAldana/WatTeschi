from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_Usuarios = models.AutoField(primary_key=True,db_column='Id_Usuario')
    Nombre_Usuario = models.TextField(unique=True,db_column='Nombre_Usuario')
    Contrasena = models.TextField(db_column='Contrasena')
    Nombre = models.TextField(db_column='Nombre')
    Apellido_Pa = models.CharField(max_length=20,db_column='Apellido_P')
    Correo = models.EmailField(unique=True,db_column='Correo')
    class Meta:
        db_table='Usuarios'

class Genero(models.Model):
    id_Genero = models.AutoField(primary_key=True,db_column='Id_Categoria')
    Descripcion = models.TextField(unique=True,db_column='Descripcion')
    class Meta:
        db_table='Generos'
class Pais(models.Model):
    Id_Pais = models.AutoField(primary_key=True,db_column='Id_Pais')
    Descripcion = models.TextField(db_column='Descripcion')
    Codigo_Pais = models.TextField(db_column='Codigo_Pais')
    class Meta:
        db_table='Paises'
class Idioma(models.Model):
    Id_Idioma = models.AutoField(primary_key=True,db_column='Id_Idioma')
    Descripcion = models.TextField(unique=True,db_column='Descripcion')
    Codigo_Idioma = models.TextField(db_column='Codigo_Idioma')
    class Meta:
        db_table='Idiomas'
class Editorial(models.Model):
    Id_Editorial = models.AutoField(primary_key=True,db_column='Id_Editorial')
    Fk_Id_pais = models.ForeignKey(Pais,on_delete=models.CASCADE,default=1,db_column='fk_pais')
    Nombre_Editorial = models.TextField(db_column='Nombre_Editorial')
    Sitio_Web = models.URLField(db_column='Sitio_Web')
    class Meta:
        db_table='Editoriales'
class Autor(models.Model):
    Id_Autor = models.AutoField(primary_key=True,db_column='Id_Autor')
    Fk_Id_pais = models.ForeignKey(Pais,on_delete=models.CASCADE,default=1,db_column='fk_pais')
    Nombre = models.CharField(max_length=25,db_column='Nombre')
    Apellido_P = models.CharField(max_length=20,db_column='Apellido_P')
    Apellido_M = models.CharField(max_length=20,db_column='Apellido_M')
    Biografia = models.CharField(max_length=200,db_column='Biografia')
    class Meta:
        db_table='Autores'
class Libro(models.Model):
    Id_Libro = models.AutoField(primary_key=True,db_column='Id_Libro')
    Fk_Id_Autor = models.ForeignKey(Autor,on_delete=models.CASCADE,default=1,db_column='fk_id_Autor')
    Fk_Id_Genero = models.ForeignKey(Genero,on_delete=models.CASCADE,default=1,db_column='fk_id_Genero')
    Fk_Id_Editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE,default=1,db_column='fk_id_Editorial')
    Fk_Id_Idioma= models.ForeignKey(Idioma,on_delete=models.CASCADE,default=1,db_column='fk_id_Idioma')
    Fecha_Publicacion = models.DateField(db_column='Fecha_Registro')
    Titulo = models.TextField(max_length=250,db_column='Titulo')
    Sinopsis = models.CharField(max_length=300,db_column='Sinopsis')
    class Meta:
        db_table='Libros'
class Resena(models.Model):
    Id_Resena = models.AutoField(primary_key=True,db_column='Id_Resena')
    Fk_Id_Libro = models.ForeignKey(Libro,on_delete=models.CASCADE,default=1,db_column='Fk_Id_Libro')
    Fk_Id_Usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,default=1,db_column='Fk_Id_Usuario')
    calificacion = models.IntegerField(db_column='Calificacion')
    Comentario = models.CharField(max_length=150,db_column='Comentario')
    class Meta:
        db_table='Resena'
class Lista_Deseos(models.Model):
    id_Lista_Deseos = models.AutoField(primary_key=True,db_column='Id_Lista_Deseos')
    Fk_Id_Libro = models.ForeignKey(Libro,on_delete=models.CASCADE,default=1,db_column='Fk_Id_Libro')
    Fk_Id_Usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,default=1,db_column='Fk_Id_Usuario')
    Fecha_Agregado = models.DateTimeField(db_column='Fecha_Agregado')
    class Meta:
        db_table='Lista_Deseados'
class Bibilioteca(models.Model):
    Id_Biblioteca = models.AutoField(primary_key=True,db_column='Id_Biblioteca')
    Fk_Id_Libro = models.ForeignKey(Libro,on_delete=models.CASCADE,default=1,db_column='Fk_Id_Libro')
    Fk_Id_Usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,default=1,db_column='Fk_Id_Usuario')
    Fecha_Inicio = models.DateTimeField(db_column='Fecha_Inicio')
    class Meta:
        db_table='Biblioteca'

class Libro_has_Autor(models.Model):
    Id_Libro_has_Autor = models.AutoField(primary_key=True,db_column='Id_Libro_has_Autor')
    Fk_Id_Libro = models.ForeignKey(Libro,on_delete=models.CASCADE,db_column='Fk_Id_Libro')
    Fk_Id_Autor = models.ForeignKey(Autor,on_delete=models.CASCADE,db_column='Fk_Id_Autor')
    class Meta:
        db_table='Libro_has_Autor'

class Libro_has_Idioma(models.Model):
    Id_Libro_has_Idioma = models.AutoField(primary_key=True,db_column='Id_Libro_has_Idioma')
    Fk_Id_Libro = models.ForeignKey(Libro,on_delete=models.CASCADE,db_column='Fk_Id_Libro')
    Fk_Id_Idioma = models.ForeignKey(Idioma,on_delete=models.CASCADE,db_column='Fk_Id_Idioma')
    class Meta:
        db_table='Libro_has_Idioma'

class Libro_has_Genero(models.Model):
    Id_Libro_has_Genero = models.AutoField(primary_key=True,db_column='Id_Libro_has_Genero')
    Fk_Id_Libro = models.ForeignKey(Libro,on_delete=models.CASCADE,db_column='Fk_Id_Libro')
    Fk_Id_Genero = models.ForeignKey(Genero,on_delete=models.CASCADE,db_column='Fk_Id_Genero')
    class Meta:
        db_table='Libro_has_Genero'



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