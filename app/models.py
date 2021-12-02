from django.db import models


class Enquete(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()

    def __str__(self):
        return self.titulo


class Resposta(models.Model):
    enquete = models.ForeignKey(
        Enquete,
        on_delete=models.CASCADE,
        related_name="respostas",
    )
    opcao = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.opcao
