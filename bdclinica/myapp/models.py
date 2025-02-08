from django.db import models
from django.contrib.auth.models import User,Group
import django_tables2 as tables
from django.urls import reverse
from django_tables2.utils import A
from django.utils.html import format_html

class Paciente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Paciente")
    data_nascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")

    def clean(self):
        if self.data_nascimento and self.data_nascimento > date.today():
            raise ValidationError("A data de nascimento não pode ser no futuro.")

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username
    
    @property
    def primeiro_nome(self):
        return self.usuario.first_name
    
    @property
    def ultimo_nome(self):
        return self.usuario.last_name

    @property
    def email(self):
        return self.usuario.email
    
    @property
    def data_cadastro(self):
        return self.usuario.date_joined

class Medico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Medico")
    data_nascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")

    def clean(self):
        if self.data_nascimento and self.data_nascimento > date.today():
            raise ValidationError("A data de nascimento não pode ser no futuro.")

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username
    
    @property
    def primeiro_nome(self):
        return self.usuario.first_name
    
    @property
    def ultimo_nome(self):
        return self.usuario.last_name

    @property
    def email(self):
        return self.usuario.email
    
    @property
    def data_cadastro(self):
        return self.usuario.date_joined

class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Funcionario")
    data_nascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")

    def clean(self):
        if self.data_nascimento and self.data_nascimento > date.today():
            raise ValidationError("A data de nascimento não pode ser no futuro.")

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username
    
    @property
    def primeiro_nome(self):
        return self.usuario.first_name
    
    @property
    def ultimo_nome(self):
        return self.usuario.last_name

    @property
    def email(self):
        return self.usuario.email
    
    @property
    def data_cadastro(self):
        return self.usuario.date_joined
    
class Procedimento(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name="Nome")
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, verbose_name="paciente"
    )
    medico = models.ForeignKey(
        Medico, on_delete=models.SET_NULL, null=True, verbose_name="medico"
    )
    data = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True) 
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome','data']

            