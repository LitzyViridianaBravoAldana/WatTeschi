# En tu archivo tests.py dentro de la carpeta de tu aplicación

import pytest
from api.models import Pais

@pytest.mark.django_db
def test_creacion_pais():
    # Crea un objeto Pais en la base de datos
    pais = Pais.objects.create(
        Descripcion="13.256753",
        Codigo_Pais="HT"
    )

    # Verifica que haya un único objeto Pais en la base de datos
    assert Pais.objects.count() == 1

    # Verifica que el atributo Id_Pais no sea nulo
    assert pais.Id_Pais is not None

    # Verifica que la descripción sea la que se estableció al crear el objeto
    assert pais.Descripcion == "13.256753"

    # Verifica que el código del país sea el que se estableció al crear el objeto
    assert pais.Codigo_Pais == "HT"
