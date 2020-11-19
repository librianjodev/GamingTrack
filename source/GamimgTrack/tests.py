import django
django.setup()

from django.test import TestCase
from GamimgTrack.models import *

from GamimgTrack.views_user import upgradar_conta, criar_conta

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