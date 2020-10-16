from django.contrib import admin
from .models import Post, Comentario, Curtida,Curtida_comentario, Seguidor

class Seguidores(admin.ModelAdmin):
    list_display = ('id', 'user','seguid')
    list_display_links = ('user','seguid')
    search_fields = ('id','user','seguid')
    list_per_page = 20

class Posts(admin.ModelAdmin):
    list_display = ('id','titulo','descricao','audio','datetime','postador')
    list_display_links = ('titulo','descricao')
    search_fields = ('titulo','descricao')
    list_per_page = 20

class Comentarios(admin.ModelAdmin):
    list_display = ('id','conteudo','datetime','postador','post')
    list_display_links = ()
    search_fields = ()
    list_per_page = 20

class Curtidas(admin.ModelAdmin):
    list_display = ('id','curtida','datetime','curtidor','post')
    list_display_links = ('curtida','datetime','curtidor','post')
    search_fields = ('curtida','datetime','curtidor','post')
    list_per_page = 20

class Curtidas_comentario (admin.ModelAdmin):
    list_display = ('id','curtida','datetime','curtidor','comentario')
    list_display_links = ('curtida','datetime','curtidor','comentario')
    search_fields = ('curtida','datetime','curtidor','comentario')
    list_per_page = 20

admin.site.register(Seguidor, Seguidores)
admin.site.register(Post, Posts)
admin.site.register(Comentario, Comentarios)
admin.site.register(Curtida, Curtidas)
admin.site.register(Curtida_comentario, Curtidas_comentario)


