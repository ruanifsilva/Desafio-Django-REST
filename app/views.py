from django.shortcuts import render, get_object_or_404
from .models import Enquete, Resposta
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# importações para REST

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EnqueteSerializer, RespostaSerializer
from django_filters.rest_framework import DjangoFilterBackend




class Index(ListView):
    template_name = 'app/index.html'
    context_object_name = 'lista_enquetes'

    def get_queryset(self):
        return Enquete.objects.order_by('-titulo')


class Detalhes(DetailView):
    model = Enquete
    template_name = 'app/detalhe_enquete.html'
    context_object_name = 'enquete'


# class ResultadoEnquete(Index):
#     template_name = 'app/resultado_enquete.html'
#     context_object_name = 'enquete'


def resultado_enquete(request, detalhe_id):
    enquete = get_object_or_404(Enquete, id=detalhe_id)

    if request.method != 'POST':
        return render(request, 'app/delhate_enquete.html')

    resposta = request.POST.get('resposta')
    resposta_selecionada = enquete.respostas.get(id=resposta)
    resposta_selecionada.votos += 1
    resposta_selecionada.save()

    return render(request, 'app/resultado_enquete.html', {'enquete': enquete})


class EnqueteViewSet(viewsets.ModelViewSet):
    queryset = Enquete.objects.all().order_by('-titulo')
    serializer_class = EnqueteSerializer
    permission_classes = [permissions.IsAuthenticated]


class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
    filter_backends = [DjangoFilterBackend]
