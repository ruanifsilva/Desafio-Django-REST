from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "app"

router = routers.DefaultRouter()
router.register(r"enquetes", views.EnqueteViewSet)
router.register(r"respostas", views.RespostaViewSet)

urlpatterns = [
    path("", views.EnqueteList.as_view(), name="index"),
    path("enquetes/<int:pk>/", views.EnqueteDetail.as_view(), name="detalhes"),
    path("enquetes/<int:pk>/votar/", views.ContarVotoView.as_view(), name="votar"),
    path(
        "enquetes/<int:pk>/resultado/",
        views.ResultadoEnqueteDetail.as_view(),
        name="resultado",
    ),
    # Django REST_framework
    path(r"api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
