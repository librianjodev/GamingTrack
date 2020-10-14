from django.shortcuts import render
from .forms import registerUserForm, loginUserForm, changeUserPasswordForm, changeUserEmailForm, changeUserNameForm
from django.http import HttpResponseRedirect, JsonResponse

from .models import User

def registerUser(response):
    if response.method == "POST":
        form = registerUserForm(response.POST)

        if form.is_valid():
            #create(first_name="Bruce", last_name="Springsteen")
            n = form.cleaned_data["nome"] # n recebe o nome do usuario
            em = form.cleaned_data["email"]
            lo = form.cleaned_data["login"]
            p = form.cleaned_data["password"]
            p1 = form.cleaned_data["password1"]
            if p != p1:
                return JsonResponse(data = {"message": "Erro: Senhas diferentes"})
            if User.objects.filter(login=lo).count() == 0:
                User.objects.create(email=em, login=lo, password=p, nome=n)
                form = loginUserForm()
                return render(response, "user/login.html", {"form":form})
            else:
                return JsonResponse(data = {"message": "E-mail já registrado no site"})

    else:
        form = registerUserForm()
        return render(response, "user/register.html", {"form":form})
def loginUser(response):
    sla = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = loginUserForm(response.POST)

        if form.is_valid():
            lo = form.cleaned_data["login"]
            p = form.cleaned_data["password"]
            if User.objects.filter(login=lo).count() == 0:
                    return JsonResponse(data = {"message": "E-mail não registrado no site"})
            if User.objects.filter(login=lo, password=p).count() == 0:
                return JsonResponse(data = {"message": "Login ou senha incorretos"})
            else:
                sla = User.objects.get(login=lo, password=p)
                response.session['id_user'] = sla.id
                return render(response, "user/info.html", {"user":sla})
    else:
        form = loginUserForm()
        return render(response, "user/login.html", {"form":form})
def alterarSenhaUser(response):
    sla = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = changeUserPasswordForm(response.POST)

        if form.is_valid():
            p = form.cleaned_data["password"]
            p1 = form.cleaned_data["password1"]
            p2 = form.cleaned_data["password2"]
            if (sla.password == p2) and (p == p1):
                sla.password = p
                sla.save()
                return render(response, "user/info.html", {"user":sla})
            else:
                return JsonResponse(data = {"message": "Algo de errado não está certo"})
    else:
        form = changeUserPasswordForm()
        return render(response, "user/alterar.html", {"form":form})

def alterarNomeUser(response):
    sla = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = changeUserNameForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data['nome']
            p = form.cleaned_data['password']
            if (sla.password == p):
                sla.nome = n
                sla.save()
                return render(response, "user/info.html", {"user":sla})
            else:
                return JsonResponse(data = {"message": "Senha incorreta"})
    else:
        form = changeUserNameForm()
        return render(response, "user/alterar.html", {"form":form})

def alterarLoginUser(response):
    sla = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = changeUserEmailForm(response.POST)

        if form.is_valid():
            p = form.cleaned_data["password"]
            e = form.cleaned_data['email']
            if (sla.password == p):
                sla.email = e
                sla.save()
                return render(response, "user/info.html", {"user":sla})
            else:
                return JsonResponse(data = {"message": "Algo de errado não está certo"})
    else:
        form = changeUserEmailForm()
        return render(response, "user/alterar.html", {"form":form})

def deletarUser(response):
    sla = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = changeUserEmailForm(response.POST)

        if form.is_valid():
            em = form.cleaned_data["email"]
            p = form.cleaned_data["password"]
            if (sla.password == p) and (sla.email == em):
                sla.delete()
                form = loginUserForm()
                return render(response, "user/login.html", {"form":form})
            else:
                return JsonResponse(data = {"message": "Algo de errado não está certo"})
    else:
        form = changeUserEmailForm()
        return render(response, "user/alterar.html", {"form":form})
