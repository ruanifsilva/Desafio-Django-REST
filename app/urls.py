from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:detalhe_id>', views.detalhes, name='detalhes'),
    path('<int:detalhe_id>/resultado_enquete/', views.resultado_enquetes, name='resultado_enquete'),
]
