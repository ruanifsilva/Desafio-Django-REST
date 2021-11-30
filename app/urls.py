from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'app'

router = routers.DefaultRouter()
router.register(r'enquetes', views.EnqueteViewSet)
router.register(r'respostas', views.RespostaViewSet)

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>/', views.Detalhes.as_view(), name='detalhes'),
    path('<int:pk>/resultado/', views.ResultadoEnquete.as_view(), name='resultado'),
    path('<int:detalhe_id>/resultado_enquete/', views.resultado_enquete, name='resultado_enquete'),
    path(r'api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
