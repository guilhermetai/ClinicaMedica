import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html
from .models import Procedimento
class procedimento_table(tables.Table):
    nome = tables.LinkColumn("procedimento_update_alias", args=[A("pk")])
    paciente = tables.Column()
    medico = tables.Column()
    data = tables.Column()
    descricao = tables.Column()
    id = tables.LinkColumn("procedimento_delete_alias", args=[A("pk")], 
    verbose_name="Excluir")
    class Meta:
        model = Procedimento
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nome', 'paciente', 'medico', 'data', 'descricao')