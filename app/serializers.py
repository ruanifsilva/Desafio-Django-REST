from .models import Enquete, Resposta
from rest_framework import serializers


class EnqueteSerializer(serializers.HyperlinkedModelSerializer):
    respostas = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Resposta.objects.all()
    )
    class Meta:
        model = Enquete
        fields = ['id', 'titulo', 'texto', 'respostas']


class RespostaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resposta
        fields = ['id', 'opcao', 'votos']