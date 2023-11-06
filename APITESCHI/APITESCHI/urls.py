from django.urls import path
from api.views import sign_in, sign_up, index_9, team, biblioteca, genero1, genero2, genero3, genero4, genero5 , genero6, genero7, genero8, genero9, genero10, editorial1, editorial2, editorial3, editorial4, favoritos, password_recovery, graficas
#from tasks import views

urlpatterns = [
    # Ruta para la página index_9
    #path('index_9.html', index_9.as_view(), name='index_9'),
    path('index_9/', index_9.as_view(), name='index_9'),


    # Ruta para la URL raíz (puede ser una de las páginas anteriores)
    #path('', index_9.as_view(), name='index_9_root'),

    # Ruta para la página de inicio de sesión
    path('sign_in/', sign_in.as_view(), name='sign_in'),
    
    # Ruta para la página de registro
    path('sign_up/', sign_up.as_view(), name='sign_up'),
    #path('sign_up.html', views.sign_up, name='sign_up'),
    
    # Ruta para la página de Team de autores
    path('team/', team.as_view(), name='team'),

    # Ruta para la página de Team de autores
    path('biblioteca/', biblioteca.as_view(), name='biblioteca'),

    # Ruta para la página de Team de autores
    path('genero1/', genero1.as_view(), name='genero1'),

    # Ruta para la página de Team de autores
    path('genero2/', genero2.as_view(), name='genero2'),

    # Ruta para la página de Team de autores
    path('genero3/', genero3.as_view(), name='genero3'),

    # Ruta para la página de Team de autores
    path('genero4/', genero4.as_view(), name='genero4'),

    # Ruta para la página de Team de autores
    path('genero5/', genero5.as_view(), name='genero5'),

    # Ruta para la página de Team de autores
    path('genero6/', genero6.as_view(), name='genero6'),

    # Ruta para la página de Team de autores
    path('genero7/', genero7.as_view(), name='genero7'),

    # Ruta para la página de Team de autores
    path('genero8/', genero8.as_view(), name='genero8'),

    # Ruta para la página de Team de autores
    path('genero9/', genero9.as_view(), name='genero9'),

    # Ruta para la página de Team de autores
    path('genero10/', genero10.as_view(), name='genero10'),

     # Ruta para la página de Team de autores
    path('editorial1/', editorial1.as_view(), name='editorial1'),

     # Ruta para la página de Team de autores
    path('editorial2/', editorial2.as_view(), name='editorial2'),

     # Ruta para la página de Team de autores
    path('editorial3/', editorial3.as_view(), name='editorial3'),

     # Ruta para la página de Team de autores
    path('editorial4/', editorial4.as_view(), name='editorial4'),

    # Ruta para la página de Team de autores
    path('favoritos/', favoritos.as_view(), name='favoritos'),

    # Ruta para la página de Team de autores
    path('password_recovery/', password_recovery.as_view(), name='password_recovery'),

    
    # Ruta para la página de Team de autores
    path('graficas/', graficas.as_view(), name='graficas'),
]
