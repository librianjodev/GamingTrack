from django.urls import path
from GamimgTrack import views

urlpatterns = [
    path('register/', views.registerUser), 
    path('', views.loginUser), 
    path('changePass/', views.alterarSenhaUser), 
    path('changeName/', views.alterarLoginUser), 
    path('changeEmail/', views.alterarNomeUser), 
    path('deleteUser/', views.deletarUser), 
    path('listarUsers/', views.ListarUsuarios), 
]
