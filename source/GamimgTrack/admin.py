from django.contrib import admin

from .models import User, Postagem, LikePostagens
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'photo', 'email', 'password', 'login', 'creationdate', 'lastlogin', 'permissionlevel')


@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('likes', 'content', 'title', 'creation_date', 'user_criador')


@admin.register(LikePostagens)
class LikePostagensAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_like', 'postagem_like')
