from django.forms import ModelForm
from .models import *


class studentform(ModelForm):
    
    class Meta:
        model = studentmodel
        fields = "__all__"

        