from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
   
    def __str__(self):
        # Exibir o nome completo (first_name + last_name) ou apenas o username
        return f"{self.usuario.first_name} {self.usuario.last_name}" if self.usuario.first_name and self.usuario.last_name else self.usuario.username
    
    def get_email(self):
        # Retorna o e-mail do usuário associado
        return self.usuario.email

    get_email.short_description = 'Email'


class Medico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        # Exibir o nome completo (first_name + last_name) ou apenas o username
        return f"{self.usuario.first_name} {self.usuario.last_name}" if self.usuario.first_name and self.usuario.last_name else self.usuario.username

    def get_email(self):
        # Retorna o e-mail do usuário associado
        return self.usuario.email

    get_email.short_description = 'Email'

class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
   
    def __str__(self):
        # Exibir o nome completo (first_name + last_name) ou apenas o username
        return f"{self.usuario.first_name} {self.usuario.last_name}" if self.usuario.first_name and self.usuario.last_name else self.usuario.username
    
    def get_email(self):
        # Retorna o e-mail do usuário associado
        return self.usuario.email
        
    get_email.short_description = 'Email'    

class Procedimento(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome','data']
            