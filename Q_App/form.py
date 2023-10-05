import json
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UploadJSONForm(forms.Form):
    archivo_json = forms.FileField(label='Seleccionar Archivo JSON', help_text='Archivos JSON solamente.')

    def __init__(self, *args, **kwargs):
        super(UploadJSONForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'cargar_json'  # Nombre de la vista a la que deseas dirigir la solicitud
        self.helper.add_input(Submit('submit', 'Enviar'))

class RespuestasForm(forms.Form):
    respuesta_1 = forms.CharField(
        label='Respuesta 1',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    respuesta_2 = forms.CharField(
        label='Respuesta 2',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    respuesta_3 = forms.CharField(
        label='Respuesta 3',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )