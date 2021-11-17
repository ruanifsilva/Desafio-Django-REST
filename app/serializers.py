from .models import Enquete
from rest_framework import serializers


class EnqueteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enquete
        fields = ['titulo', 'texto', 'opcao', 'votos']
