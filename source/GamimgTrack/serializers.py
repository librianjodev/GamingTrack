from rest_framework import serializers
from .models import LikePostagens, Postagem, User, Game, ComentariosPostagens, Review


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True},
            'password': {'write_only': True}
        }
        model = User
        fields = (
            'id',
            'nome',
            'photo',
            'email',
            'password',
            'login',
            'creationdate',
            'last_login',
            'permissionlevel',
            'is_staff',
            'is_superuser',
        )


class PostagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Postagem
        fields = (
            'id',
            'likes',
            'content',
            'title',
            'creation_date',
            'user_criador',
        )


class LikePostagensSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikePostagens
        fields = (
            'id',
            'user_like',
            'postagem_like',
        )


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = (
            'id',
            'name',
            'relative_image',
            'description',
            'save_date'
        )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'likes',
            'content',
            'title',
            'creation_date',
            'user_criador'
        )


class ComentariosPostagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentariosPostagens
        fielders = (
            'id',
            'user',
            'postagem',
            'comentario'
        )
