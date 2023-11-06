# render es para renderizar y redirect para redireccionar
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Usuario
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.hashers import check_password, make_password
from django.utils.html import strip_tags
import random
import string
from .models import  encuestaSatisfaccion # Asegúrate de importar tu modelo
import csv 
# importaciones para graficos
from django.db.models import Count
# Create your views here.



class index_9(APIView):
    template_name="index_9.html"
    def get(self,request):
        return render(request,self.template_name)

from django.contrib.auth.hashers import make_password

class sign_up(APIView):
    template_name = "sign_up.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # Obtenemos los datos del formulario
        nombre_usuario = request.POST.get('Usuario', '')
        contra1 = request.POST.get('Contra1', '')
        contra2 = request.POST.get('Contra2', '')
        nombre = request.POST.get('Nombre', '')
        apellido_pa = request.POST.get('ApellidoPa', '')
        correo = request.POST.get('Correo', '')

        # Verificamos si las contraseñas son iguales
        if contra1 != contra2:
           return render(request, self.template_name, {'error': 'La Contraseña no es la misma, verifique'})

        try:
            # Creamos una instancia de Usuario con los datos del formulario
            user = Usuario(
                Nombre_Usuario=nombre_usuario,
                Nombre=nombre,
                Apellido_Pa=apellido_pa,
                Correo=correo,
                Contrasena=contra1
            )

            # Establecemos la contraseña utilizando make_password
            user.Contrasena = make_password(contra1)

            # Guardamos el usuario en la base de datos
            user.save()

            # Enviamos un correo de bienvenida
            subject = 'Registro para TeschiWATT'
            message = 'Bienvenido a TESCHIWATT, gracias por registrarte en la página de libros más variada para ti'
            from_email = 'teschiwatt@gmail.com'
            recipient_list = [request.POST.get('Correo', '')]

            # Utiliza la plantilla de correo electrónico HTML
            html_message = render_to_string('correo_b.html', {'username': nombre_usuario, 'password': contra1})

            send_mail(subject, message, from_email, recipient_list, html_message=html_message)

            # Redirigimos a la página de inicio de sesión
            return redirect('sign_in')

        except Exception as e:
            # Manejar cualquier excepción y mostrar el mensaje de error apropiado
            return render(request, self.template_name, {'error': f'Error al registrar usuario: {e}'})


# INCIO DE CODIGO PARA INICIAR SESIÓN

class sign_in(APIView):

    template_name = "sign_in.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        # Inicio de codigo para importacion csv de cuestionario

        # archivo_csv = 'C:/Users/Litzy Aldana/Music/Base de datos/Encuesta.csv'  # Ruta al archivo CSV que deseas importar
        
        # with open(archivo_csv, 'r', encoding='utf-8') as file:
        #     csv_reader = csv.DictReader(file)
        #     for row in csv_reader:
        #         nuevo_registro = encuestaSatisfaccion(
        #             correo=row['Dirección de correo electrónico'],
        #             pregunta1=row['¿Qué tipo de paleta de colores prefieres para el diseño del sistema web de la biblioteca?'],
        #             pregunta2=row['¿Qué opinas sobre la personalización de tu perfil en el sistema web de la biblioteca?'],
        #             pregunta3=row['¿Cómo te gustaría que se presenten los resultados de búsqueda en el sistema web de la biblioteca?'],
        #             pregunta4=row['¿Cuál de las siguientes opciones de búsqueda preferirías en el sistema web de la biblioteca?'],
        #             pregunta5=row['¿Qué función consideras más importante para un acceso rápido en la página principal del sistema web de la biblioteca?'],
        #             pregunta6=row['¿Dónde preferirías ver las notificaciones en el sistema web de la biblioteca?'],
        #             pregunta7=row['¿Te gustaría poder personalizar las notificaciones que recibes en el sistema web de la biblioteca?']
        #             # Asigna los campos y columnas correspondientes
        #         )
        #         nuevo_registro.save()
        # return render(request, 'index_9.html')

        # fin de codigo de cuestioanrio

        if "acceso" in request.POST:

            # Procesar Login

            email = request.POST.get("correo")
            password1 = request.POST.get("password")
            # Buscar un usuario con el correo electrónico proporcionado
            try:

                usuario = Usuario.objects.get(Correo=email)  # , password=password1
                print('correo', usuario)
                # usuario = authenticate(request, correoElectronico=email, password=password1)

                valorObtenido = usuario.Correo

            except Usuario.DoesNotExist:

                valorObtenido = None
            # usuario = authenticate(request, correElectronico=email, password=password1)
            contra = usuario.Contrasena
            if valorObtenido is not None:
                # La contraseña es correcta, inicia sesión
                # login(request, usuario)
                if check_password(password1, contra):

                    return redirect("index_9")  # Redirige a la página 'home' después del inicio de sesión

                else:

                    mensaje = "Credenciales incorrectas. Por favor, inténtalo de nuevo. Contraseña"

                    return render(request, self.template_name, {"error": mensaje})
            else:

                mensaje = "Credenciales incorrectas. Por favor, inténtalo de nuevo. CORREO"

                return render(request, self.template_name, {"error": mensaje})

            # Lógica de login aquí
# FIN DE CODIGO PARA INICIO DE SESIÓN






class team(APIView):
    template_name="team.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class biblioteca(APIView):
    template_name="biblioteca.html"
    def get(self,request):
        return render(request,self.template_name) 
    

class genero1(APIView):
    template_name="genero1.html"
    def get(self,request):
        return render(request,self.template_name) 
    

class genero2(APIView):
    template_name="genero2.html"
    def get(self,request):
        return render(request,self.template_name) 
    

class genero3(APIView):
    template_name="genero3.html"
    def get(self,request):
        return render(request,self.template_name) 
    

class genero4(APIView):
    template_name="genero4.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class genero5(APIView):
    template_name="genero5.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class genero6(APIView):
    template_name="genero6.html"
    def get(self,request):
        return render(request,self.template_name) 
    

class genero7(APIView):
    template_name="genero7.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class genero8(APIView):
    template_name="genero8.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class genero9(APIView):
    template_name="genero9.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class genero10(APIView):
    template_name="genero10.html"
    def get(self,request):
        return render(request,self.template_name) 
    
    
class editorial1(APIView):
    template_name="editorial1.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class editorial2(APIView):
    template_name="editorial2.html"
    def get(self,request):
        return render(request,self.template_name) 

class editorial3(APIView):
    template_name="editorial3.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class editorial4(APIView):
    template_name="editorial4.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class favoritos(APIView):
    template_name="favoritos.html"
    def get(self,request):
        return render(request,self.template_name) 
    
#GRAFICAS
class graficas(APIView):
    template_name="graficas.html"
    def post(self,request):
        return render(request, self.template_name)

    def get(self, request):
    
            # Pregunta 1
            respuestas1 = encuestaSatisfaccion.objects.values('pregunta1').annotate(total=Count('pregunta1'))
            etiquetas1 = [respuesta['pregunta1'] for respuesta in respuestas1]
            valores1 = [respuesta['total'] for respuesta in respuestas1]
    
            # Pregunta 2
            respuestas2 = encuestaSatisfaccion.objects.values('pregunta2').annotate(total=Count('pregunta2'))
            etiquetas2 = [respuesta['pregunta2'] for respuesta in respuestas2]
            valores2 = [respuesta['total'] for respuesta in respuestas2]
    
            # Pregunta 3
            respuestas3 = encuestaSatisfaccion.objects.values('pregunta3').annotate(total=Count('pregunta3'))
            etiquetas3 = [respuesta['pregunta3'] for respuesta in respuestas3]
            valores3 = [respuesta['total'] for respuesta in respuestas3]
    
            # Pregunta 4
            respuestas4 = encuestaSatisfaccion.objects.values('pregunta4').annotate(total=Count('pregunta4'))
            etiquetas4 = [respuesta['pregunta4'] for respuesta in respuestas4]
            valores4 = [respuesta['total'] for respuesta in respuestas4]
    
            # Pregunta 5
            respuestas5 = encuestaSatisfaccion.objects.values('pregunta5').annotate(total=Count('pregunta5'))
            etiquetas5 = [respuesta['pregunta5'] for respuesta in respuestas5]
            valores5 = [respuesta['total'] for respuesta in respuestas5]
    
            # Pregunta 6
            respuestas6 = encuestaSatisfaccion.objects.values('pregunta6').annotate(total=Count('pregunta6'))
            etiquetas6 = [respuesta['pregunta6'] for respuesta in respuestas6]
            valores6 = [respuesta['total'] for respuesta in respuestas6]
    
            # Pregunta 7
            respuestas7 = encuestaSatisfaccion.objects.values('pregunta7').annotate(total=Count('pregunta7'))
            etiquetas7 = [respuesta['pregunta7'] for respuesta in respuestas7]
            valores7 = [respuesta['total'] for respuesta in respuestas7]
    
    
    
            # Pasa los datos a la plantilla
            return render(request, self.template_name, {'etiquetasPregunta1': etiquetas1,
                                                        'valoresPregunta1': valores1,
                                                    'etiquetasPregunta2': etiquetas2,
                                                    'valoresPregunta2': valores2,
                                                    'etiquetasPregunta3': etiquetas3,
                                                    'valoresPregunta3': valores3,
                                                    'etiquetasPregunta4': etiquetas4,
                                                    'valoresPregunta4': valores4,
                                                    'etiquetasPregunta5': etiquetas5,
                                                    'valoresPregunta5': valores5,
                                                    'etiquetasPregunta6': etiquetas6,
                                                    'valoresPregunta6': valores6,
                                                    'etiquetasPregunta7': etiquetas7,
                                                    'valoresPregunta7': valores7})
#fin de graficas    
    
    
class password_recovery(APIView):
    template_name="password_recovery.html"
    def get(self,request):
        return render(request,self.template_name) 
    def post(self,request):
        if "recupera" in request.POST:
            # Recuperar pasword
            email = request.POST["re_correo"]

            # Verifica si el correo ya existe en la base de datos

            if Usuario.objects.filter(Correo=email).exists():
                # Obtén un usuario específico por su correo electrónico

                usuario = Usuario.objects.get(Correo=email)
                # Genera una contraseña aleatoria de 12 caracteres que incluye letras mayúsculas, letras minúsculas y dígitos
                nueva_contrasena = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
                # Almacena la contraseña aleatoria como la nueva contraseña del usuario (debes cifrarla)
                usuario.Contrasena = make_password(nueva_contrasena)
                # Guarda el usuario en la base de datos para actualizar la contraseña
                usuario.save()
                # Luego, prepara y envía el correo electrónico

                subject = "WATTESCHI Recuperación de Contraseña"

                from_email = "teschiwatt@gmail.com"

                recipient_list = [request.POST["re_correo"]]

                # Utiliza la plantilla HTML para el correo electrónico

                html_message = render_to_string("correo_p.html",{

                                    "new_password": " "

                                    + nueva_contrasena

                                },

                            )

                            # {{nombre}} es como se llama la variable que mandamos
                            # Envía el correo electrónico

                send_mail(subject,strip_tags(html_message),from_email,recipient_list,html_message=html_message,)

                return redirect("sign_in")

        else:

            mensaje = "Lo siento el correo no existe"

            return render(request, self.template_name, {"mensajeo": mensaje})

        # Logica de recuperacion de pasword



