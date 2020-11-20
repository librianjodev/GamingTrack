from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms_reviews import CriarReviewForm
from .models import Review, User
from .views_user import IrParaVisita, IrParaInicio
from .views_comentarios import pegar_comentarios

MENS_ERROR = "Algo de errado não está certo"
CRIAR_REVIEW = "reviews/criar_review.html"
GOTO_LIST_REVIEW = "reviews/lista_review.html"
VER_REVIEW = "reviews/ver_review.html"
EDIR_REVIEW = "reviews/editar_review.html"
INFO = "user/info.html"


def criar_nova_review(response):
    logado = User.objects.get(id=response.session['id_user'])
    if response.method == "POST":
        form = CriarReviewForm(response.POST)
        if form.is_valid():
            post = Review.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                user_criador=logado
            )
            post.save()
            return render(
                response, VER_REVIEW,
                {
                    "user": logado, "post": post,
                    "criador": post.user_criador,
                    "lista_comentarios": None
                }
            )
        return JsonResponse(data={"message": MENS_ERROR})
    else:
        form = CriarReviewForm()
        return render(response, CRIAR_REVIEW, {"form": form})


def listar_review(response):
    logado = User.objects.get(id=response.session['id_user'])
    if response.method == 'POST':
        if "visitar" in response.POST:
            visitar = Review.objects.get(id=response.session['id_postagem']).user_criador
            if visitar == logado:
                return render(response, INFO, {"user": logado})
            upgradar = ["Comum", '', "Tutor", "Moderador", "Administrador"]
            return render(
                response, IrParaVisita,
                {"user": logado,
                 "visita": visitar,
                 "upgradar": upgradar
                 }
            )
        elif "apagar" in response.POST:
            p = Review.objects.get(id=response.session['id_postagem'])
            p.delete()
            return render(response, IrParaInicio, {"user": logado})
        # Verifica se o botão pressionado foi o botão de Pesquisar
        elif "pesquisar" in response.POST:
            lista = []
            filtro = response.POST.get('filtro')
            for reviews in Review.objects.filter(title__contains=filtro):
                lista_local = []
                lista_local.append(reviews.title)
                lista_local.append(reviews.id)
                lista.append(lista_local)
                # Ele filtra pela pesquisa por nome
            return render(response, GOTO_LIST_REVIEW, {'lista': lista})
#        elif "comentar" in response.POST:
#            visitar = Review.objects.get(id=response.session['id_postagem'])
#            <ComentarioReview>.objects.create(postagem=visitar, user=logado,
#                                                comentario=response.POST.get('comentario')).save()
#            comentarios = pegar_comentarios(visitar.id)
#            return render(response, ver_postagem, {"user": logado, "post": visitar, "lista_comentarios": comentarios})
        for i in Review.objects.all():
            if str(i.id) in response.POST:
                visitar = i
                response.session['id_postagem'] = visitar.id
                criador = visitar.user_criador
                comentarios = pegar_comentarios(visitar.id)
                return render(
                    response, VER_REVIEW,
                    {
                        "user": logado,
                        "post": visitar,
                        "criador": criador,
                        "lista_comentarios": comentarios
                    }
                )
        return JsonResponse(data={"message": MENS_ERROR})
    else:
        lista = []
        #filtro = response.POST.get('filtro')
        for reviews in Review.objects.all():
            lista_local = []
            lista_local.append(reviews.title)
            lista_local.append(reviews.id)
            lista.append(lista_local)
            # Ele filtra pela pesquisa por nome
        return render(response, GOTO_LIST_REVIEW, {'lista': lista})


def mostrar_reviews_visita(response):
    visitante = User.objects.get(id=response.session['id_visita'])
    lista = []
    if response.method == "POST":
        for i in Review.objects.all():
            if str(i.id) in response.POST:
                visitar = i
                response.session['id_postagem'] = visitar.id
                criador = visitar.user_criador
                comentarios = pegar_comentarios(visitar.id)
                return render(
                    response, VER_REVIEW,
                    {
                        "user": visitante,
                        "post": visitar,
                        "criador": criador,
                        "lista_comentarios": comentarios
                    }
                )
        filtro = response.POST.get('filtro')
        for reviews in Review.objects.filter(user_criador=visitante, title__contains=filtro):
            lista_local = []
            lista_local.append(reviews.title)
            lista_local.append(reviews.id)
            lista.append(lista_local)
        return render(response, GOTO_LIST_REVIEW, {'lista': lista})
    for reviews in Review.objects.filter(user_criador=visitante):
        lista_local = []
        lista_local.append(reviews.title)
        lista_local.append(reviews.id)
        lista.append(lista_local)
    return render(response, GOTO_LIST_REVIEW, {'lista': lista})
