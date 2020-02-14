from django.db import models

# Codice Cliente (id),
# Codice Fiscale,
# Ragione Sociale/Cognome,
# Nome,
# Indirizzo,
# Cap,
# Comune,
# Provincia,
# Codice Stato (IT),
# Email

class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    codice_fiscale = models.CharField(max_length=20)
    ragione_cognome = models.CharField(max_length=128)
    nome = models.CharField(max_length=64)
    indirizzo = models.CharField(max_length=128)
    cap = models.IntegerField()
    comune = models.CharField(max_length=64)
    provincia = models.CharField(max_length=64)
    stato = models.CharField(max_length=2)
    email = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.id}:{self.codice_fiscale}, {self.nome}"