from rest_framework import viewsets, generics
from .models import Post, Comentario, Curtida,Curtida_comentario, Seguidor
from .serializer import PostSerializer, ComentarioSerializer, CurtidaSerializer, Curtida_comentarioSerializer, SeguidorSerializer, ListaseguidoresSerializer, ListaseguidosSerializer


class SeguidoresViewSet(viewsets.ModelViewSet):
    """seguindo uma pessoa nova"""
    queryset = Seguidor.objects.all()
    page_size = 10
    serializer_class = SeguidorSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
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