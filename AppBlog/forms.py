from django import forms

class DiseñadoresFormulario(forms.Form):

    nombre= forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()

class EmpresasFormulario(forms.Form):

    nombre= forms.CharField()
    ubicacion= forms.CharField()
       
class DiseñosFormulario(forms.Form):

    modelo= forms.CharField()
    autor= forms.CharField()   