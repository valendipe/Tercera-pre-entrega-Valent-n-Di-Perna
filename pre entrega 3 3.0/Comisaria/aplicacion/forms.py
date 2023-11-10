from django import forms

class ComisariaInsertar(forms.Form):
    nombre= forms.CharField(required=True, max_length=256)
    numero= forms.IntegerField(required=True, max_value=150)

class PoliciaInsertar(forms.Form):
    apellido = forms.CharField(required=True, max_length=256)
    nombre = forms.CharField(required=True, max_length=256)
    telefono = forms.CharField(max_length=20)

class DetenidoInsertar(forms.Form):
    apellido = forms.CharField(required=True, max_length=256)
    nombre = forms.CharField(required=True, max_length=256)
    motivo_de_detencion=forms.CharField(max_length=500)
    dni= forms.IntegerField()
    fecha_de_nacimiento= forms.DateField()