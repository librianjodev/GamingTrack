from django import forms

class registerUserForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=255)
    email = forms.CharField(label="E-mail", max_length=255)
    login = forms.CharField(required=False)
    password = forms.CharField(max_length=255, label="senha")
    password1 = forms.CharField(max_length=255, label="repetir senha")
    check = forms.BooleanField(label="Você está de acordo com os nossos termos?")