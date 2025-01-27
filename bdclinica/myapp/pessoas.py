import django_tables2 as tables
from django.urls import reverse
from django_tables2.utils import A
from django.contrib.auth.models import User,Group
from django.utils.html import format_html

class UserTable(tables.Table):
    username = tables.LinkColumn("user_update_alias", args=[A("pk")], verbose_name="Usuário")
    email = tables.Column(verbose_name="Email")
    first_name = tables.Column(verbose_name="Primeiro Nome")
    last_name = tables.Column(verbose_name="Sobrenome")
    groups = tables.Column(verbose_name="Grupos", accessor='groups__name', orderable=False)
    actions = tables.Column(empty_values=(), verbose_name="Ações")

    def render_groups(self, record):
        return ', '.join(group.name for group in record.groups.all())

    def render_actions(self, record):
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm">Editar</a> '
            '<a href="{}" class="btn btn-danger btn-sm">Excluir</a>',
            reverse('user_update_alias', args=[record.pk]),
            reverse('user_delete_alias', args=[record.pk])
        )

    class Meta:
        model = User
        attrs = {"class": "table table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('username', 'email', 'first_name', 'last_name', 'groups')