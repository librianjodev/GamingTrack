from django.contrib import admin

from .models import User, Postagem, LikePostagens, Game, Review, ComentariosPostagens


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'photo', 'email', 'password', 'login', 'creationdate', 'last_login', 'permissionlevel')


@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('likes', 'content', 'title', 'creation_date', 'user_criador')


@admin.register(LikePostagens)
class LikePostagensAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_like', 'postagem_like')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('relative_image', 'name', 'description', 'save_date')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('likes', 'content', 'title', 'creation_date', 'user_criador')


@admin.register(ComentariosPostagens)
class ComentariosPostagensAdmin(admin.ModelAdmin):
    list_display = ('user', 'postagem', 'comentario')
