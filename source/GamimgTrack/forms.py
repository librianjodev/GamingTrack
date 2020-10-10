from django import forms

class registerUserForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=255)
    check = forms.BooleanField()