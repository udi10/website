from django import forms
from django.forms import ModelForm
from myapp.models import Emp




class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = "__all__"