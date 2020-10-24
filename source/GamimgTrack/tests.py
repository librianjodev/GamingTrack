import django
django.setup()

from django.test import TestCase
from GamimgTrack.models import User

# Create your tests here.

class UserTests(TestCase):
    
    def test_verificaDataCriacao(self):
        u = User.objects.create(email='teste', login='login', password='null', nome='Teste')
        u.save()
        self.assertIsNotNone(u.creationdate)