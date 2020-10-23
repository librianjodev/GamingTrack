from django.urls import path
from GamimgTrack import views_user

urlpatterns = [
    path('register/', views_user.RegisterUser), 
    path('', views_user.LoginUser), 
    path('changeMyPass/', views_user.AlterarSenhaUser), 
    path('changeMyName/', views_user.AlterarLoginUser), 
    path('changeMyEmail/', views_user.AlterarNomeUser), 
    path('deleteMyUser/', views_user.DeletarMinhaConta), 
    path('listarUsers/', views_user.ListarUsuarios),
    path('apagarConta/', views_user.ApagarOutraConta),
]
