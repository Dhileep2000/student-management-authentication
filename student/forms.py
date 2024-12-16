from django import forms
from .models import *

class studentform(forms.ModelForm):
    class Meta:
        model = studentmodel
        fields = "__all__"
        labels = {'fname': "First Name", 'lname': "Last Name", 'phone': "Phone no"}
        widgets = {
            'fname': forms.TextInput(attrs={"class": "form-control-lg"}),
            'lname': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'phone': forms.NumberInput(attrs={"class": "form-control"}),
            'branch': forms.Select(attrs={"class": "form-control"}),
        }
