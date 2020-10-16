from django.contrib import admin
from django.urls import path,include
from core.views import PostsViewSet, ComentariosViewSet, CurtidasViewSet, Curtida_comentariosViewSet, SeguidoresViewSet, Listaseguidores, Listaseguidos
from rest_framework import routers
from user.views import Userviewset

router = routers.DefaultRouter()
router.register('usuarios', Userviewset, basename='Usuarios')
router.register('seguidores', SeguidoresViewSet, basename='Seguidores')
router.register('posts', PostsViewSet, basename='Posts')
router.register('comentarios',ComentariosViewSet, basename='Comentarios')
router.register('curtidas', CurtidasViewSet, basename='Curtidas')
router.register('curtidas_comentarios', Curtida_comentariosViewSet, basename='Curtidas_comentarios')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('usuarios/<int:pk>/seguidores/', Listaseguidores.as_view()),
    path('usuarios/<int:pk>/seguidos/', Listaseguidos.as_view()),
]
