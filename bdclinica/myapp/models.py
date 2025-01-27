from django.db import models
from django.contrib.auth.models import User

class UsuarioBase(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}" if self.usuario.first_name and self.usuario.last_name else self.usuario.username

    def get_email(self):
        return self.usuario.email

    get_email.short_description = "Email"

class Paciente(UsuarioBase):
    data_nascimento = models.DateField()

    def clean(self):
        if self.data_nascimento > models.DateField().today():
            raise ValidationError("A data de nascimento não pode ser no futuro.")

class Medico(UsuarioBase):
    especialidade = models.CharField(max_length=100, verbose_name="Especialidade", blank=True, null=True)

class Funcionario(UsuarioBase):
    data_nascimento = models.DateField()

    def clean(self):
        if self.data_nascimento > models.DateField().today():
            raise ValidationError("A data de nascimento não pode ser no futuro.")  

class Procedimento(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True)
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome','data']
            