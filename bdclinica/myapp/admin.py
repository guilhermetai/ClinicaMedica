from django.contrib import admin
from .models import Paciente, Medico, Funcionario

# Registro dos modelos no admin
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('usuario','primeiro_nome','ultimo_nome', 'data_cadastro', 'data_nascimento')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')
    ordering = ['usuario']

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('usuario','primeiro_nome','ultimo_nome' ,'data_cadastro', 'data_nascimento')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')
    ordering = ['usuario']

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('usuario','primeiro_nome','ultimo_nome' ,'data_cadastro', 'data_nascimento')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')
    ordering = ['usuario']