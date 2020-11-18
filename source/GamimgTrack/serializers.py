from rest_framework import serializers
from .models import LikePostagens, Postagem, User, Game


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
            'lastlogin',
            'permissionlevel',
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


class ReviewSerializer(serializers.ModelSerialize):
    class Meta:
        model = Game
        fields = (
            'id',
            'likes',
            'content',
            'title',
            'creation_date',
            'user_criador'
        )
