from rest_framework import generics, exceptions, status

from .serializers import PostagemSerializer, UserSerializer, LikePostagensSerializer, ReviewSerializer

from .models import Postagem, User, LikePostagens, Review

'''
List, Create
'''


class PostagensAPIView(generics.ListCreateAPIView):
        queryset = Postagem.objects.all()
        serializer_class = PostagemSerializer

        def get_queryset(self):
            if self.kwargs.get('pk'):
                return self.queryset.filter(user_id=self.kwargs.get('pk'))
            return self.queryset.all()


class UsersAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LikePostagensAPIView(generics.ListCreateAPIView):
    queryset = LikePostagens.objects.all()
    serializer_class = LikePostagensSerializer


class ReviewAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

'''
Delete, Update

'''


class PostagemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LikePostagemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LikePostagens.objects.all()
    serializer_class = LikePostagensSerializer


class ReviewAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
