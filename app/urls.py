from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>', views.Detalhes.as_view(), name='detalhes'),
    # path('resultado_enquete/<int:pk>/', views.ResultadoEnquete.as_view(), name='resultado'),
    path('resultado_enquete/<int:detalhe_id>/', views.resultado_enquete, name='resultado_enquete'),
]
