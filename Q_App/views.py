import os
from django.conf import settings
from django.shortcuts import redirect, render
from django.shortcuts import render
from Q_App.form import RespuestasForm, UploadJSONForm
import json

 
preguntas = []  
# Create your views here.
def inicio(request):
    form = UploadJSONForm
    return render(request,'pages/home.html', {'form': form})

def cargar_json(request): 
     
    if request.method == 'POST': 
        form = UploadJSONForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_json = request.FILES['archivo_json']
            ruta_archivo = os.path.join(settings.MEDIA_ROOT, 'files_loads', archivo_json.name)
            try:
                 # Guarda el archivo en la ubicación deseada
                with open(ruta_archivo, 'wb') as file:
                 for chunk in archivo_json.chunks():
                    file.write(chunk)
 
                with open(ruta_archivo, 'r') as json_file:
                 preguntas = json.load(json_file)
                
                
                print("Archivo JSON cargado con éxito:")
                #form = RespuestasForm(preguntas=preguntas)
         
            except json.JSONDecodeError:
                print("Error: El archivo no es válido JSON.")
    else:
        print('aaa')
        form = UploadJSONForm()
    
    return render(request, 'pages/home.html', {'form': form, 'preguntas': preguntas}) 
 

def procesar_respuestas(request):
    if request.method == 'POST': 
        form = RespuestasForm(request.POST)  
        if form.is_valid():   
            respuestas_usuario = form.cleaned_data  # Obtén las respuestas del formulario
            puntuacion = 0  # Inicializa la puntuación  
            
            # Obtén las preguntas de contexto
            preguntas = request.POST.getlist('pregunta')  # Asegúrate de que 'pregunta' sea el nombre correcto en tu HTML
            with open("C:/Users/user/Desktop/APPS AND PAGES WEB/Django/Questions/files_loads/preguntas.json", 'r') as json_file:
             preguntas = json.load(json_file)
             
            # Compara las respuestas del usuario con las respuestas correctas
            for pregunta in preguntas: 
                id_pregunta = pregunta['id']  # Convierte el id a cadena
                respuesta_usuario = respuestas_usuario.get('respuesta_' + str(id_pregunta), '').strip()
                respuesta_correcta = pregunta['respuesta_correcta'].strip() 

                if respuesta_usuario.lower() == respuesta_correcta.lower(): 
                    # La respuesta del usuario coincide con la respuesta correcta (sin distinguir mayúsculas/ minúsculas)
                    puntuacion += 1  # Aumenta la puntuación

            # Puedes realizar cualquier otro procesamiento necesario con la puntuación
            # Por ejemplo, guardar la puntuación en la base de datos, generar un informe, etc.

            # Redirige a una página de resultados o muestra la puntuación
            print(puntuacion)
            return render(request, 'pages/home.html', {'form': form,'puntuacion': puntuacion})     
        else:
            print('mal')

    # Si no se envió un formulario válido o no se envió un formulario POST, redirige a la página de inicio u otra página
    return redirect('inicio')