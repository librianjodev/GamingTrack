from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ComentariosPostagens, Postagem, User, Review, ComentariosReview
from .views_reviews import VER_REVIEW, pegar_comentarios_Reviews

MensagemErro = "Algo de errado não está certo"
editarOuApagarComentarioPost = "comments/editarApagarEmPostagem.html"
editarOuApagarComentarioReview = "comments/editarApagarEmReview.html"
ver_postagem = "posts/ver_postagem.html"

# Comentários Postagens
def editar_apagar_comentario_postagem(response):
    logado = User.objects.get(id=response.session['id_user'])
    if response.method == 'POST':
        if "save" in response.POST:
            comentario = ComentariosPostagens.objects.get(id=response.session['id_comentario'])
            comentario.comentario = response.POST.get('comment')
            comentario.save()
        elif "apagar" in response.POST:
            ComentariosPostagens.objects.get(id=response.session['id_comentario']).delete()
        else:
            for i in ComentariosPostagens.objects.all():
                if str(i.id) in response.POST:
                    response.session['id_comentario'] = i.id
                    return render(response, editarOuApagarComentarioPost, {"comentario": i.comentario})
        comentarios = pegar_comentarios_Postagens(response.session['id_postagem'])
        return render(response, ver_postagem, {"user":logado, "post": Postagem.objects.get(id=response.session['id_postagem']), "lista_comentarios":comentarios})

def adm_ou_criador_apaga_comentario_em_post(response):
    logado = User.objects.get(id=response.session['id_user'])
    if response.method == 'POST':
        postagem = Postagem.objects.get(id=response.session['id_postagem'])
        for i in ComentariosPostagens.objects.filter(postagem=postagem):
            if str(i.id) in response.POST:
                i.delete()
                comentarios = pegar_comentarios_Postagens(response.session['id_postagem'])
                return render(response, ver_postagem, {"user":logado, "post": postagem, "lista_comentarios":comentarios})
    return JsonResponse(data={"message": MensagemErro})

def pegar_comentarios_Postagens(idPostagem):
    comentarios = []
    visitar = Postagem.objects.get(id=idPostagem)
    for i in ComentariosPostagens.objects.filter(postagem=visitar):
        """
        0 = nome do criador do comentario
        1 = comentário em si
        2 = id do comentário
        3 = criador do comentário
        4 = criador da postagem
        """
        sla = []
        #[nome, comentário, idComentario, idUser, id criador da postagem]
        sla.append(i.user.nome)
        sla.append(i.comentario)
        sla.append(i.id)
        sla.append(i.user.id)
        sla.append(visitar.user_criador.id)
        comentarios.append(sla)
    return comentarios

# Comentarios reviews

def adm_ou_criador_apaga_comentario_em_review(response):
    logado = User.objects.get(id=response.session['id_user'])
    if response.method == 'POST':
        review = Review.objects.get(id=response.session['id_review'])
        for i in ComentariosReview.objects.filter(review=review):
            if str(i.id) in response.POST:
                i.delete()
                comentarios = pegar_comentarios_Reviews(response.session['id_review'])
                return render(response, VER_REVIEW, {"user":logado, "post": review, "lista_comentarios":comentarios})
    return JsonResponse(data={"message": MensagemErro})

def editar_apagar_comentario_review(response):
    logado = User.objects.get(id=response.session['id_user'])
    if response.method == 'POST':
        if "save" in response.POST:
            comentario = ComentariosReview.objects.get(id=response.session['id_comentario'])
            comentario.comentario = response.POST.get('comment')
            comentario.save()
        elif "apagar" in response.POST:
            ComentariosReview.objects.get(id=response.session['id_comentario']).delete()
        else:
            for i in ComentariosReview.objects.all():
                if str(i.id) in response.POST:
                    response.session['id_comentario'] = i.id
                    return render(response, editarOuApagarComentarioReview, {"comentario": i.comentario})
        comentarios = pegar_comentarios_Reviews(response.session['id_postagem'])
        return render(response, ver_postagem, {"user":logado, "post": Review.objects.get(id=response.session['id_review']), "lista_comentarios":comentarios})