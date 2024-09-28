from django.db import models

class Usuario(models.Model):
    # ID único para cada usuário; gerado automaticamente pelo Django
    id_usuario = models.AutoField(primary_key=True)

    # Campo para armazenar o nome do usuário
    # O uso de TextField aqui não é necessário, 
    # você pode usar CharField com um max_length
    nome = models.CharField(max_length=255)  # Corrigido para CharField

    # Campo para armazenar a senha do usuário
    # É recomendável usar um método de hashing em vez de armazenar senhas como texto simples
    senha = models.CharField(max_length=255)  # Corrigido para CharField

    # Campo para armazenar o email do usuário
    email = models.EmailField(max_length=255)  # Corrigido para EmailField

    # Campo para armazenar o telefone do usuário
    telefone = models.CharField(max_length=15)  # Corrigido para CharField, para incluir DDD e formato

    def __str__(self):
        return self.nome  # Representação do objeto como string, útil para admin e debugging

    from django.db import models

from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    telefone = models.IntegerField()

