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