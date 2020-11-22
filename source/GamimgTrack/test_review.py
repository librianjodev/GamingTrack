import django
django.setup()

from django.test import TestCase
from .models import *

import random


class ReviewTests(TestCase):
    def test_son_delete_set_default(self):
        usuario = User.objects.create(nome='Guilherme', email='gui@email.com', login='guipg', password='alfa3')
        usuario.save()
        review = Review.objects.create(content='test', title='testar', user_criador=usuario)
        review.save()
        self.assertIsNotNone(review.user_criador)
        usuario.delete()  # Ao deletar, o criador deve se tornar null
        self.assertIsNone(review.user_criador.id)
        review.delete()

    def test_fazer_varias_reviews(self):
        for x in range(random.randint(1, 30)):
            # Quantos posts serao criados?
            titulo = criar_frase_aleatoria(random.randint(1, 50))
            conteudo = criar_frase_aleatoria(random.randint(1, 400))
            # print("Titulo do post: "+titulo+" Conteúdo:\n"+conteudo)
            post = Review.objects.create(content=conteudo, title=titulo)
            self.assertIsNotNone(post.creation_date)

def criar_frase_aleatoria(tamanho_da_frase):
    letras = ['a', 'b', 'c', 'd', 'e', ' ', 'f', 'g', 'h', 'i', 'j', ' ', 'k', 'l', 'm', 'n', ' ', 'o', 'p', 'q',
              'r', ' ', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    palavra = ''
    for i in range(tamanho_da_frase):
        palavra += random.choice(letras)
    return palavra
