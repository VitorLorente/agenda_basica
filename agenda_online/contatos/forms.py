from django.forms import ModelForm
from .models import *

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'