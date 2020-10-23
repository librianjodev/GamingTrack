from django.urls import path
from GamimgTrack import views

urlpatterns = [
    path('register/', views.RegisterUser), 
    path('', views.LoginUser), 
    path('changeMyPass/', views.AlterarSenhaUser), 
    path('changeMyName/', views.AlterarLoginUser), 
    path('changeMyEmail/', views.AlterarNomeUser), 
    path('deleteMyUser/', views.DeletarMinhaConta), 
    path('listarUsers/', views.ListarUsuarios),
    path('apagarConta/', views.ApagarOutraConta),
]
