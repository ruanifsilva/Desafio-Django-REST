from django.shortcuts import render, get_object_or_404
from .models import Enquete


def index(request):
    lista_enquetes = Enquete.objects.order_by('-titulo')
    return render(request, 'app/index.html', {'lista_enquetes': lista_enquetes})


def detalhes(request, detalhe_id):
    enquete = get_object_or_404(Enquete, id=detalhe_id)
    return render(request, 'app/detalhe_enquete.html', {'enquete': enquete})


def resultado_enquetes(request, detalhe_id):
    enquete = get_object_or_404(Enquete, id=detalhe_id)

    if request.method != 'POST':
        return render(request, 'app/delhate_enquete.html')

    resposta = request.POST.get('resposta')
    resposta_selecionada = enquete.resposta_set.get(id=resposta)
    resposta_selecionada.votos += 1
    resposta_selecionada.save()

    return render(request, 'app/resultado_enquete.html', {'enquete': enquete})
