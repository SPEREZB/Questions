# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos (requirements.txt) al contenedor
COPY requirements.txt .
 
# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el código de tu aplicación al contenedor
COPY . .

# Expone el puerto 8000 para la aplicación Django
EXPOSE 8000

# Inicia la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]