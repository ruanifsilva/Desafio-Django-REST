from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, reverse
from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets

from .models import Enquete, Resposta
from .serializers import EnqueteSerializer, RespostaSerializer


class EnqueteList(generic.ListView):
    model = Enquete
    template_name = "app/index.html"
    context_object_name = "lista_enquetes"
    ordering = ["-titulo"]


class EnqueteDetail(generic.DetailView):
    model = Enquete
    template_name = "app/detalhe_enquete.html"
    context_object_name = "enquete"


class ResultadoEnqueteDetail(generic.DetailView):
    model = Enquete
    template_name = "app/resultado_enquete.html"


class ContarVotoView(generic.View):
    def post(self, request, **kwargs):
        enquete = get_object_or_404(Enquete, id=kwargs.get("pk"))
        resposta = request.POST.get("resposta")

        if not resposta:
            messages.info(request, "Vai se fuder sua mula do caralho.")
            return redirect("app:detalhes", pk=enquete.id)

        resposta_selecionada = enquete.respostas.get(id=resposta)
        resposta_selecionada.votos += 1
        resposta_selecionada.save()

        return redirect(reverse("app:resultado", kwargs={"pk": enquete.id}))


class EnqueteViewSet(viewsets.ModelViewSet):
    queryset = Enquete.objects.all().order_by("-titulo")
    serializer_class = EnqueteSerializer
    permission_classes = [permissions.IsAuthenticated]


class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
    filter_backends = [DjangoFilterBackend]
