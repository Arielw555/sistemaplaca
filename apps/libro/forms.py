from django  import forms
from .models import Placas

class PlacasForm1 (forms.ModelForm):
    class Meta:
        model= Placas
        fields = [
            'nombre',
            'No_cedula',
            'chasis',
            'noPlaca',
            'compania',
            'fechaOrden',
            'endoso',
            'FechaEndoso',
            'Estado',
            'cedula',
            'Comentario',
            
            

        ]