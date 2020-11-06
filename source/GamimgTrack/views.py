from rest_framework import generics, exceptions, status

from .serializers import PostagemSerializer, UserSerializer, LikePostagensSerializer


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
