import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html
from django.urls import reverse
from .models import Procedimento

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
           ## '<form action="{}" method="POST" style="display:inline;">'
           ## '{% csrf_token %}'
            '<button type="submit" class="btn btn-danger btn-sm">Excluir</button>',
          ##  '</form>',
            reverse('procedimento_update_alias', args=[record.pk]),
            reverse('procedimento_delete_alias', args=[record.pk])
    )

    
    class Meta:
        model = Procedimento
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nome', 'paciente', 'medico', 'data', 'descricao')

        