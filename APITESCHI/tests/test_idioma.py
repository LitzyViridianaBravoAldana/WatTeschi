# En tu archivo tests.py dentro de la carpeta de tu aplicación

import pytest
from api.models import Idioma

@pytest.mark.django_db
def test_consulta_idioma():
    # Crea un objeto Idioma en la base de datos
    idioma = Idioma.objects.create(
        Descripcion="Inglés",
        Codigo_Idioma="en"
    )

    # Consulta el objeto Idioma desde la base de datos
    idioma_recuperado = Idioma.objects.get(Descripcion="Inglés")

    # Verifica que el objeto recuperado sea el mismo que el objeto creado
    assert idioma_recuperado == idioma

@pytest.mark.django_db
def test_actualizacion_idioma():
    # Crea un objeto Idioma en la base de datos
    idioma = Idioma.objects.create(
        Descripcion="Francés",
        Codigo_Idioma="fr"
    )

    # Actualiza la descripción del idioma
    idioma.Descripcion = "Francés canadiense"
    idioma.save()

    # Recupera el objeto actualizado desde la base de datos
    idioma_actualizado = Idioma.objects.get(Codigo_Idioma="fr")

    # Verifica que la descripción del idioma se haya actualizado correctamente
    assert idioma_actualizado.Descripcion == "Francés canadiense"

@pytest.mark.django_db
def test_eliminacion_idioma():
    # Crea un objeto Idioma en la base de datos
    idioma = Idioma.objects.create(
        Descripcion="Alemán",
        Codigo_Idioma="de1@"
    )

    # Elimina el objeto Idioma de la base de datos
    idioma.delete()

    # Intenta recuperar el objeto eliminado y verifica que no existe
    with pytest.raises(Idioma.DoesNotExist):
        Idioma.objects.get(Codigo_Idioma="de1@")
