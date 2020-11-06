from django.urls import path
from . import views_user, views_postagens, views

urlpatterns = [
    # Django API REST framework
    path('usuario/', views.UsersAPIView.as_view(), name='usuarios'),
    path('postagem/', views.PostagensAPIView.as_view(), name='postagens'),
    path('like/', views.LikePostagensAPIView.as_view(), name='likes'),

    path('usuario/<int:pk>/postagem/', views.PostagemAPIView.as_view(), name='usuario_postagens'),

    path('usuario/<int:pk>/', views.UserAPIView.as_view(), name='usuario'),
    path('postagem/<int:pk>/', views.PostagemAPIView.as_view(), name='postagem'),
    path('like/<int:pk>/', views.LikePostagemAPIView.as_view(), name='like'),

    #Pure Django Framework
    path('register/', views_user.RegisterUser),
    path('info/', views_user.mostrar_detalhes),
    path('', views_user.LoginUser),
    path('changeMyPass/', views_user.AlterarSenhaUser),
    path('changeMyName/', views_user.AlterarLoginUser),
    path('changeMyEmail/', views_user.AlterarNomeUser),
    path('deleteMyUser/', views_user.DeletarMinhaConta),
    path('listarUsers/', views_user.ListarUsuarios),
    path('listarPostagens/', views_postagens.listar_postagens),
    path('apagarConta/', views_user.ApagarOutraConta),
    path('meusPosts/', views_user.mostrar_meus_posts),

    path('criarNovaPostagem/', views_postagens.criar_nova_postagem),
]
