from django.shortcuts import render, redirect
from django.http import JsonResponse

MensagemErro = "Algo de errado não está certo"

def criar_nova_postagem(response):

    return JsonResponse(data = {"message": MensagemErro})