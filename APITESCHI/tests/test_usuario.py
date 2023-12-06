# En tu archivo tests.py dentro de la carpeta de tu aplicación

import pytest
from api.models import Usuario

@pytest.mark.django_db
def test_creacion_usuario():
    # Crea un objeto Usuario en la base de datos
    usuario = Usuario.objects.create(
        Nombre_Usuario="11",
        Contrasena="contrasena123",
        Nombre="Nombre@gmail.com",
        Apellido_Pa="Apellido12345678910111213141515",
        Correo="147"
    )

    # Verifica que haya un único objeto Usuario en la base de datos
    assert Usuario.objects.count() == 1

    # Verifica que el atributo id_Usuarios no sea nulo
    assert usuario.id_Usuarios is not None

    # Verifica que el nombre de usuario sea el que se estableció al crear el objeto
    assert usuario.Nombre_Usuario == "11"

    # Verifica que la contraseña sea la que se estableció al crear el objeto
    assert usuario.Contrasena == "contrasena123"

    # Verifica que el nombre sea el que se estableció al crear el objeto
    assert usuario.Nombre == "Nombre@gmail.com"

    # Verifica que el apellido sea el que se estableció al crear el objeto
    assert usuario.Apellido_Pa == "Apellido12345678910111213141515"

    # Verifica que el correo sea el que se estableció al crear el objeto
    assert usuario.Correo == "147"
