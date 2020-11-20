import django
django.setup()

from django.test import TestCase
from GamimgTrack.models import *

from GamimgTrack.views_user import upgradar_conta, criar_conta, deletar_outra_conta

import random
# Create your tests here.

class UserTests(TestCase):
    
    def test_verificar_data_de_criacao(self):
        u = User.objects.create(email='teste', login='login', password='null', nome='Teste')
        u.save()
        self.assertIsNotNone(u.creationdate)
        u.delete()
    
    def test_upgrade_de_conta(self):
        logado = User.objects.create(nome='logado', email='nenhum@gmail.com', login='Sou Foda', password='Pra caralho')
        conta_para_upgradar = User.objects.create(email='teste', login='login', password='null', nome='Teste')
        self.assertEquals(0, upgradar_conta(logado, conta_para_upgradar, 4)) # Usuário comum tentando fazer outro usuário virar moderador
        # Isso não irá acontecer no site, visto que tal botão sequer aparece na página
        logado.permissionlevel = 3
        self.assertEquals(0, upgradar_conta(logado, conta_para_upgradar, 4)) # Usuário Tutor tentando fazer outro usuário virar moderador, não deve dar certo
        logado.permissionlevel = 4
        self.assertNotEquals(0, upgradar_conta(logado, conta_para_upgradar, 4)) # Usuário Moderador tentando fazer outro usuário virar moderador
    
    def test_criacao_de_contas(self):
        # Vamos criar um Usuário X e tentar cadastrar outro usando o mesmo e-mail, para cadastrar o outro vamos verificar pela mesma forma que é verificada no site
        self.assertEquals(0, criar_conta("nome", 'email', 'login', 'senha', 'repetir_senha')) # Tentativa de criar conta com senhas diferente, deve tetornar 0
        user2 = User.objects.create(nome='logado', email='nenhum@gmail.com', login='Sou Foda', password='Pra caralho')
        user2.save()
        self.assertEquals(2, criar_conta("nome", 'nenhum@gmail.com', 'login', 'senha', 'senha')) # Tentativa de criar onta com um e-mail já cadastrado
        self.assertEquals(2, criar_conta("nome", 'email', 'Sou Foda', 'senha', 'senha')) # Tentativa de criar onta com um login já usadp
        self.assertEquals(1, criar_conta("nome", 'email', 'login', 'senha', 'senha')) # Criação de conta permitida
        user2.delete()
    
    def test_deletar_outras_contas(self):
        self.assertEquals(0, 0)
        user = User.objects.create(nome='logado', email='nenhum', login='Sou Foda', password='Pra caralho')
        user2 = User.objects.create(nome='aDeletar', email='sla@gmail.com', login='Idiota com I maiusculo', password='sim')
        self.assertEquals(0, deletar_outra_conta(user.permissionlevel, user2.permissionlevel)) # não poderá apagar a outra conta visto que o user não tem o nível de permissão para tal ação
        user.permissionlevel = 4
        user2.permissionlevel = 5
        self.assertEquals(0, deletar_outra_conta(user.permissionlevel, user2.permissionlevel)) # não poderá apagar a outra conta visto que o user tem um nível de poder menor que o do user2
        user.permissionlevel = 5
        self.assertEquals(1, deletar_outra_conta(user.permissionlevel, user2.permissionlevel)) # agora deu certo

class PostagensTests(TestCase):
    def test_set_null_on_delete(self):
        u = User.objects.create(nome='criador', email='não tenho', login='login', password='123')
        u.save()
        p = Postagem.objects.create(content='test', title='testar', user_criador=u)
        p.save()
        self.assertIsNotNone(p.user_criador) 
        u.delete() # Ao deletar, o criador deve se tornar null
        self.assertIsNone(p.user_criador.id)
        p.delete()
    
    def test_criar_postagens_aleatórias(self):
        for x in range(random.randint(1, 200)):
            # Quantos posts serao criados?
            titulo = criar_frase_aleatoria(random.randint(1, 50))
            conteudo = criar_frase_aleatoria(random.randint(1, 1000))
            #print("Titulo do post: "+titulo+" Conteúdo:\n"+conteudo)
            post = Postagem.objects.create(content=conteudo, title=titulo)
            self.assertIsNotNone(post.creation_date)
            
def criar_frase_aleatoria(tamanho_da_frase):
        letras = ['a', 'b', 'c', 'd', 'e', ' ', 'f', 'g', 'h', 'i', 'j', ' ', 'k', 'l', 'm', 'n', ' ', 'o', 'p', 'q', 'r', ' ', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        palavra = ''
        for i in range (tamanho_da_frase):
            palavra += random.choice(letras)
        return palavra