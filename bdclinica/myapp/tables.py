import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html
from django.urls import reverse
from .models import Procedimento
from django.contrib.auth.models import User,Group

class procedimento_table(tables.Table):
    nome = tables.LinkColumn("procedimento_update_alias", args=[A("pk")])
    paciente = tables.Column()
    medico = tables.Column()
    data = tables.Column()
    descricao = tables.Column()
    actions = tables.Column(empty_values=(), verbose_name="Ações")

    def render_actions(self, record):
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm">Editar</a> '
            '<a href="{}" class="btn btn-danger btn-sm">Excluir</a>',
            reverse('procedimento_update_alias', args=[record.pk]),
            reverse('procedimento_delete_alias', args=[record.pk])
    )

    class Meta:
        model = Procedimento
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nome', 'paciente', 'medico', 'data', 'descricao')

class UserTable(tables.Table):
    username = tables.LinkColumn("user_update_alias", args=[A("pk")], verbose_name="Usuário")
    email = tables.Column(verbose_name="Email")
    first_name = tables.Column(verbose_name="Primeiro Nome")
    last_name = tables.Column(verbose_name="Sobrenome")
    cargo = tables.Column(verbose_name="Cargo", orderable=False, )
    def render_cargo(self, record):
        print(f"DEBUG: render_cargo chamado para {record.username}")  
        user_obj=User.objects.get(username=record.username)
        user_groups=user_obj.groups.all()
        user_group=user_groups.first()
        print(f"Usuário: {record.username}, {user_group if user_group else "Sem grupo"}")
        return user_group if user_group else "Sem grupo"
    def get_cargo_value(self, record):        
        user_obj=User.objects.get(username=record.username)
        user_groups=user_obj.groups.all()
        user_group=user_groups.first()
        print(f"Usuário: {record.username}, {user_group if user_group else "Sem grupo"}")
        return user_group if user_group else "Sem grupo"
    tosco = tables.Column(verbose_name="Tosco", orderable=False, )
    
    
    actions = tables.Column(empty_values=(), verbose_name="Ações")
    def render_actions(self, record):
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm">Editar</a> '
            '<a href="{}" class="btn btn-primary btn-sm">Trocar Senha</a> '
            '<a href="{}" class="btn btn-danger btn-sm">Excluir</a>',
            reverse('user_update_alias', args=[record.pk]),
            reverse('alterar_senha_alias', args=[record.pk]),
            reverse('user_delete_alias', args=[record.pk])
        )

    class Meta:
        model = User
        attrs = {"class": "table table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('username', 'email', 'first_name', 'last_name','cargo','tosco')       
