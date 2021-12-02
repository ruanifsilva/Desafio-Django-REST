from rest_framework import serializers

from .models import Enquete, Resposta


class RespostaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resposta
        fields = ["id", "opcao", "votos"]
        extra_kwargs = {"opcao": {"required": True}}


class EnqueteSerializer(serializers.HyperlinkedModelSerializer):
    respostas = RespostaSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Enquete
        fields = ["id", "titulo", "texto", "respostas"]

    def create(self, validated_data):
        respostas = validated_data.pop("respostas")

        enquete = Enquete.objects.create(**validated_data)

        for item in respostas:
            resposta = Resposta(enquete=enquete, **item)
            resposta.save()

        return enquete
