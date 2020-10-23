from django.shortcuts import render
from .forms import RegisterUserForm, LoginUserForm, ChangeUserPasswordForm, ChangeUserEmailForm, ChangeUserNameForm
from django.http import HttpResponseRedirect, JsonResponse

from GamimgTrack.models import User

### Setando strings: 
IrParaLogin = "user/login.html"
IrParaRegistrar = "user/register.html"
IrParaInfo = "user/info.html"
IrParaAlterar = "user/alterar.html"
IrParaListarUsers = "user/lista_users.html"
IrParaVisita = "user/visitar_outro.html"
MensagemErro = "Algo de errado não está certo"

def registerUser(response):
    if response.method == "POST":
        form = RegisterUserForm(response.POST)

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
                form = LoginUserForm()
                return render(response, IrParaLogin, {"form":form})
            else:
                return JsonResponse(data = {"message": "E-mail já registrado no site"})

    else:
        form = RegisterUserForm()
        return render(response, IrParaRegistrar, {"form":form})
def loginUser(response):
    
    if response.method == "POST":
        form = LoginUserForm(response.POST)

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
                return render(response, IrParaInfo, {"user":sla})
    else:
        form = LoginUserForm()
        return render(response, IrParaLogin, {"form":form})
def alterarSenhaUser(response):
    sla = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = ChangeUserPasswordForm(response.POST)

        if form.is_valid():
            p = form.cleaned_data["password"]
            p1 = form.cleaned_data["password1"]
            p2 = form.cleaned_data["password2"]
            if (sla.password == p2) and (p == p1):
                sla.password = p
                sla.save()
                return render(response, IrParaInfo, {"user":sla})
            else:
                return JsonResponse(data = {"message": MensagemErro})
    else:
        form = ChangeUserPasswordForm()
        return render(response, IrParaAlterar, {"form":form})

def alterarNomeUser(response):
    sla = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = ChangeUserNameForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data['nome']
            p = form.cleaned_data['password']
            if (sla.password == p):
                sla.nome = n
                sla.save()
                return render(response, IrParaInfo, {"user":sla})
            else:
                return JsonResponse(data = {"message": "Senha incorreta"})
    else:
        form = ChangeUserNameForm()
        return render(response, IrParaAlterar, {"form":form})

def alterarLoginUser(response):
    sla = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = ChangeUserEmailForm(response.POST)

        if form.is_valid():
            p = form.cleaned_data["password"]
            e = form.cleaned_data['email']
            if (sla.password == p):
                sla.email = e
                sla.save()
                return render(response, IrParaInfo, {"user":sla})
            else:
                return JsonResponse(data = {"message": MensagemErro})
    else:
        form = ChangeUserEmailForm()
        return render(response, IrParaAlterar, {"form":form})

def deletarUser(response):
    sla = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = ChangeUserEmailForm(response.POST)

        if form.is_valid():
            em = form.cleaned_data["email"]
            p = form.cleaned_data["password"]
            if (sla.password == p) and (sla.email == em):
                sla.delete()
                form = LoginUserForm()
                return render(response, IrParaLogin, {"form":form})
            else:
                return JsonResponse(data = {"message": MensagemErro})
    else:
        form = ChangeUserEmailForm()
        return render(response, IrParaAlterar, {"form":form})

def ListarUsuarios(response):
    if response.method == 'POST':
        for i in range(len(User.objects.exclude(id = response.session['id_user']))):
            if str(i+1) in response.POST:
                # i+1 é o id do usuario
                visitar = User.objects.get(id=(i+1))

                return render(response, IrParaVisita, {"user":visitar})
    else:
        
        lista = []
        for users in User.objects.exclude(id = response.session['id_user']):
            sla = []
            sla.append(users.nome)
            sla.append(users.id)
            lista.append(sla)
            #lista recebe uma lista que possue sempre 2 valores, o primeiro é o nome do usuario e o segundo o seu id
        return render(response, IrParaListarUsers, {'lista': lista})
