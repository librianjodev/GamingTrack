from django.urls import path
from GamimgTrack import views_user, views_postagens, views

urlpatterns = [
    path('inicio/', views.tela_inicial),
    path('register/', views_user.RegisterUser), 
    path('info/', views_user.mostrar_detalhes),
    path('', views_user.LoginUser), 
    path('changeMyPass/', views_user.AlterarSenhaUser), 
    path('changeMyName/', views_user.AlterarLoginUser), 
    path('changeMyEmail/', views_user.AlterarNomeUser), 
    path('deleteMyUser/', views_user.DeletarMinhaConta), 
    path('listarUsers/', views_user.ListarUsuarios),
    path('apagarConta/', views_user.ApagarOutraConta),
    path('criarNovaPostagem/', views_postagens.criar_nova_postagem),
]
