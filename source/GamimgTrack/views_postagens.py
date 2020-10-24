from django.shortcuts import render, redirect
from django.http import JsonResponse

from GamimgTrack.forms_postagens import CriarPostagemForm
from GamimgTrack.models import Postagem, User

from GamimgTrack.views_user import IrParaVisita, IrParaInicio

MensagemErro = "Algo de errado não está certo"

criar_postagem = "posts/criar_post.html"
IrParaListarPostagens = "posts/lista_postagens.html"
ver_postagem = "posts/ver_postagem.html"

def criar_nova_postagem(response):
    logado = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = CriarPostagemForm(response.POST)
        if form.is_valid():
            post = Postagem.objects.create(title = form.cleaned_data['title'], content= form.cleaned_data['content'], user_criador= logado)
            post.save()
            return render(response, IrParaInicio, {"user":logado})
        return JsonResponse(data = {"message": MensagemErro})
    else:
        form = CriarPostagemForm()
        return render(response, criar_postagem, {"form":form})

def listar_postagens(response):
    logado = User.objects.get(id = response.session['id_user'])
    if response.method == 'POST':
        if "visitar" in response.POST:
            upgradar = ["Comum", '',"Tutor", "Moderador", "Administrador"]
            visitar = Postagem.objects.get(id = response.session['id_postagem']).user_criador
            return render(response, IrParaVisita, {"user":logado, "visita":visitar, "upgradar": upgradar})
        elif "apagar" in response.POST:
            Postagem.objects.get(id = response.session['id_postagem']).delete
            #return render(response, IrParaInicio, {"user":logado})
        # Verifica se o botão pressionado foi o botão de Pesquisar
        elif "pesquisar" in response.POST:
            lista = []
            filtro = response.POST.get('filtro')
            for posts in Postagem.objects.filter(title__contains=filtro):
                sla = []
                sla.append(posts.title)
                sla.append(posts.id)
                lista.append(sla)
                # Ele filtra pela pesquisa por nome
            return render(response, IrParaListarPostagens, {'lista': lista})
        for i in Postagem.objects.all():
            if str(i.id) in response.POST:
                # Aqui ele verifica se o botão pressionado tem o id do user no select
                visitar = i
                response.session['id_postagem'] = visitar.id
                criador = visitar.user_criador
                return render(response, ver_postagem, {"user":logado, "post":visitar, "criador": criador})
        return JsonResponse(data = {"message": MensagemErro})
    else:
        lista = []
        filtro = response.POST.get('filtro')
        for posts in Postagem.objects.all():
            sla = []
            sla.append(posts.title)
            sla.append(posts.id)
            lista.append(sla)
            # Ele filtra pela pesquisa por nome
        return render(response, IrParaListarPostagens, {'lista': lista})
    return JsonResponse(data = {"message": MensagemErro})