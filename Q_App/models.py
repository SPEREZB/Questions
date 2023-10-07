from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.CharField(max_length=255)

    def __str__(self):
        return self.pregunta