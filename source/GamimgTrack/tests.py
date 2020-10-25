import django
django.setup()

from django.test import TestCase
from GamimgTrack.models import *

from GamimgTrack.views_user import upgradar_conta

# Create your tests here.

class UserTests(TestCase):
    
    def test_verificar_data_de_criacao(self):
        u = User.objects.create(email='teste', login='login', password='null', nome='Teste')
        u.save()
        self.assertIsNotNone(u.creationdate)
        u.delete()
    
    def test_set_null_on_delete(self):
        u = User.objects.create(nome='criador', email='não tenho', login='login', password='123')
        u.save()
        p = Postagem.objects.create(content='test', title='testar', user_criador=u)
        p.save()
        self.assertIsNotNone(p.user_criador) 
        u.delete() # Ao deletar, o criador deve se tornar null
        self.assertIsNone(p.user_criador.id)
        p.delete()
    
    def test_upgrade_de_conta(self):
        logado = User.objects.create(nome='logado', email='nenhum@gmail.com', login='Sou Foda', password='Pra caralho')
        conta_para_upgradar = User.objects.create(email='teste', login='login', password='null', nome='Teste')
        self.assertEquals(0, upgradar_conta(logado, conta_para_upgradar, 4)) # Usuário comum tentando fazer outro usuário virar moderador
        # Isso não irá acontecer no site, visto que tal botão sequer aparece na página
        logado.permissionlevel = 3
        self.assertEquals(0, upgradar_conta(logado, conta_para_upgradar, 4)) # Usuário Tutor tentando fazer outro usuário virar moderador, não deve dar certo
        logado.permissionlevel = 4
        self.assertNotEquals(0, upgradar_conta(logado, conta_para_upgradar, 4)) # Usuário Moderador tentando fazer outro usuário virar moderador

        