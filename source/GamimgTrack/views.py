from django.shortcuts import render
from .forms import registerUserForm
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
                return HttpResponseRedirect("/") # redireciona para a página inicial do projeto
            else:
                return JsonResponse(data = {"message": "E-mail já registrado no site"})

    else:
        form = registerUserForm()
        return render(response, "user/register.html", {"form":form})


