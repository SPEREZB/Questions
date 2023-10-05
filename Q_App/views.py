from django.shortcuts import render
from django.shortcuts import render
from Q_App.form import UploadJSONForm
import json
 
# Create your views here.
def inicio(request):
    form = UploadJSONForm
    return render(request,'pages/home.html', {'form': form})

def cargar_json(request): 
    if request.method == 'POST': 
        form = UploadJSONForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_json = request.FILES['archivo_json']
            try:
                contenido_json = json.load(archivo_json)
                print("Archivo JSON cargado con éxito:")
                print(contenido_json)
            except json.JSONDecodeError:
                print("Error: El archivo no es válido JSON.")
    else:
        print('aaa')
        form = UploadJSONForm()
    
    return render(request, 'pages/home.html', {'form': form}) 