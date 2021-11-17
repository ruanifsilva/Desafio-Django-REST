from django.contrib import admin
from .models import Enquete, Resposta


class EnqueteAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo',)


class RespostaAdmin(admin.ModelAdmin):
    list_display = ('id', 'opcao', 'votos')




admin.site.register(Enquete, EnqueteAdmin)
admin.site.register(Resposta, RespostaAdmin)