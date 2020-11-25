from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms_reviews import CriarReviewForm
from .models import Review, User, ComentariosReview
VER_REVIEW = "reviews/ver_review.html"
from .views_user import IrParaVisita, IrParaInicio

MENS_ERROR = "Algo de errado não está certo"
CRIAR_REVIEW = "reviews/criar_review.html"
GOTO_LIST_REVIEW = "reviews/lista_review.html"
EDIR_REVIEW = "reviews/editar_review.html"
INFO = "user/info.html"

def pegar_comentarios_Reviews(idReview):
    comentarios = []
    visitar = Review.objects.get(id=idReview)
    for i in ComentariosReview.objects.filter(review=visitar):
        sla = []
        #[nome, comentário, idComentario, idUser, id criador da postagem]
        sla.append(i.user.nome)
        sla.append(i.comentario)
        sla.append(i.id)
        sla.append(i.user.id)
        sla.append(visitar.user_criador.id)
        comentarios.append(sla)
    return comentarios

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
            visitar = Review.objects.get(id=response.session['id_review']).user_criador
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
        if "apagar" in response.POST:
            p = Review.objects.get(id=response.session['id_review'])
            p.delete()
            return render(response, IrParaInicio, {"user": logado})
        # Verifica se o botão pressionado foi o botão de Pesquisar
        if "pesquisar" in response.POST:
            lista = []
            filtro = response.POST.get('filtro')
            for reviews in Review.objects.filter(title__contains=filtro):
                lista_local = []
                lista_local.append(reviews.title)
                lista_local.append(reviews.id)
                lista.append(lista_local)
                # Ele filtra pela pesquisa por nome
            return render(response, GOTO_LIST_REVIEW, {'lista': lista})
        if "comentar" in response.POST:
            visitar = Review.objects.get(id=response.session['id_review'])
            ComentariosReview.objects.create(review=visitar, user=logado, comentario=response.POST.get('comentario')).save()
            comentarios = pegar_comentarios_Reviews(visitar.id)
            return render(response, VER_REVIEW, {"user": logado, "post": visitar, "lista_comentarios": comentarios})
        for i in Review.objects.all():
            if str(i.id) in response.POST:
                visitar = i
                response.session['id_review'] = visitar.id
                criador = visitar.user_criador
                comentarios = pegar_comentarios_Reviews(visitar.id)
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
                response.session['id_review'] = visitar.id
                criador = visitar.user_criador
                comentarios = pegar_comentarios_Reviews(visitar.id)
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
