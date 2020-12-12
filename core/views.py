from rest_framework import viewsets, generics
from .models import Post, Comentario, Curtida,Curtida_comentario, Seguidor, Conversa, Mensagem
from .serializer import PostSerializer, ComentarioSerializer, CurtidaSerializer, Curtida_comentarioSerializer, SeguidorSerializer, ListaseguidoresSerializer, ListaseguidosSerializer
from .serializer import MensagemSerializer, ConversaSerializer
from user.models import User


class SeguidoresViewSet(viewsets.ModelViewSet):
    """seguindo uma pessoa nova"""
    queryset = Seguidor.objects.all()
    page_size = 10
    serializer_class = SeguidorSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-datetime')
    page_size = 10
    serializer_class = PostSerializer

class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    page_size = 10
    serializer_class = ComentarioSerializer

class CurtidasViewSet(viewsets.ModelViewSet):
    queryset= Curtida.objects.all()
    page_size = 10
    serializer_class = CurtidaSerializer

class Curtida_comentariosViewSet(viewsets.ModelViewSet):
    queryset= Curtida_comentario.objects.all()
    page_size = 10
    serializer_class = Curtida_comentarioSerializer

class Listaseguidores(generics.ListAPIView):
    """listando seguidores do usuario"""
    def get_queryset(self):
        queryset = Seguidor.objects.filter(user_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaseguidoresSerializer

class Listaseguidos(generics.ListAPIView):
    """listando pessoas que o usuario ta seguindo"""
    def get_queryset(self):
        queryset = Seguidor.objects.filter(seguid_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaseguidosSerializer

class  Listacomentariopost(generics.ListAPIView):
    """Listando comentarios de um post"""
    def get_queryset(self):
        queryset = Comentario.objects.order_by('-datetime').filter(post_id=self.kwargs['pk'])    
        return queryset
    serializer_class = ComentarioSerializer

class  Listaposts(generics.ListAPIView):
    """Listando posts do usuario"""
    def get_queryset(self):
        queryset = Post.objects.order_by('-datetime').filter(postador_id=self.kwargs['pk'])
        return queryset
    serializer_class = PostSerializer

class Listaseguidoresnome(generics.ListAPIView):
    """listando seguidores do usuario"""
    def get_queryset(self):
        user = User.objects.filter(username=self.kwargs['username']).get()
        queryset = Seguidor.objects.filter(user_id=self.user.id)
        return queryset
    serializer_class = ListaseguidoresSerializer

class Listaseguidosnome(generics.ListAPIView):
    """listando pessoas que o usuario ta seguindo"""
    def get_queryset(self):
        user = User.objects.filter(username=self.kwargs['username']).get()
        queryset = Seguidor.objects.filter(seguid_id=self.id)
        return queryset
    serializer_class = ListaseguidosSerializer

class  Listapostsnome(generics.ListAPIView):
    """Listando posts do usuario"""
    def get_queryset(self):
        user = User.objects.filter(username=self.kwargs['username']).get()
        queryset = Post.objects.order_by('-datetime').filter(postador_id=user.id)
        return queryset
    serializer_class = PostSerializer

class ConversaViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    page_size = 10
    serializer_class = ConversaSerializer

class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Conversa.objects.all()
    page_size = 10
    serializer_class = MensagemSerializer