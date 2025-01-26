from django.contrib import admin
from .models import *
admin.site.register(Procedimento)



class PacienteCustomizado(admin.ModelAdmin):
    list_display = ('__str__','get_email','calcula_idade')
    
    @admin.display(description='Idade')
    def calcula_idade(self, obj):
        from datetime import date
        hoje = date.today() 
        idade = hoje.year - obj.data_nascimento.year
        return idade

admin.site.register(Paciente, PacienteCustomizado)    


class MedicoCustomizado(admin.ModelAdmin):
    list_display = ('__str__','get_email',)

admin.site.register(Medico,MedicoCustomizado)

class FuncionarioCustomizado(admin.ModelAdmin):
    list_display = ('__str__','get_email',)

admin.site.register(Funcionario,FuncionarioCustomizado)