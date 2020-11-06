from django import forms


class RegisterUserForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=255)
    email = forms.CharField(label="E-mail", max_length=255)
    login = forms.CharField(required=False, max_length=255)
    password = forms.CharField(max_length=255, label="senha", widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=255, label="confirme a senha", widget=forms.PasswordInput)
    check = forms.BooleanField(label="Você está de acordo com os nossos termos?")


class LoginUserForm(forms.Form):
    login = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, label="senha", widget=forms.PasswordInput)


class ChangeUserPasswordForm(forms.Form):
    password = forms.CharField(max_length=255, label="senha", widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=255, label="confirme a nova senha", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, label="senha antiga", widget=forms.PasswordInput)


class ChangeUserEmailForm(forms.Form):
    email = forms.CharField(max_length=255, label="email atual")
    password = forms.CharField(max_length=255, label="senha", widget=forms.PasswordInput)


class ChangeUserNameForm(forms.Form):
    nome = forms.CharField(max_length=255, label="nickname")
    password = forms.CharField(max_length=255, label="senha", widget=forms.PasswordInput)
