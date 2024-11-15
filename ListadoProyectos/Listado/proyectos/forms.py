from django import forms
from proyectos.models import Proyecto

class PrincipalProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'