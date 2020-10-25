import django
django.setup()

from django.test import TestCase
from GamimgTrack.models import *

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

        