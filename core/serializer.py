from rest_framework import serializers
from .models import Post, Comentario, Curtida,Curtida_comentario, Seguidor, Conversa, Mensagem

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comentario
        fields='__all__'

class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Curtida
        fields='__all__'

class Curtida_comentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Curtida_comentario
        fields='__all__'

class  SeguidorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seguidor
        fields='__all__'

class ListaseguidoresSerializer(serializers.ModelSerializer):
    seguid = serializers.ReadOnlyField(source='seguid.username')
    class Meta:
        model=Seguidor
        fields = ['seguid']

class ListaseguidosSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model=Seguidor
        fields = ['user']

class ConversaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Conversa
        fields='__all__'

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mensagem
        fields='__all__'