from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from .models import Procedimento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import UserPassesTestMixin


# Mixin para verificar se o usuário é funcionário ou administrador
class AdminOrFuncionarioRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Funcionario').exists()

    def handle_no_permission(self):
        return HttpResponseForbidden("Apenas administradores ou funcionários podem acessar esta página.")

class AdminOrFuncionarioOrMedicoRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name__in=['Funcionario','Medico']).exists()

    def handle_no_permission(self):
        return HttpResponseForbidden("Apenas administradores ou funcionários podem acessar esta página.")

def index(request):
    usuario = request.POST.get('username')
    senha = request.POST.get('password')
    user = authenticate(username=usuario, password=senha)
    if user is not None:
        login(request, user)
        request.session['username'] = usuario
        request.session['password'] = senha
        request.session['usernamefull'] = user.get_full_name()

        # Redireciona para o Django Admin se o usuário for um superusuário
        if user.is_superuser:
            return redirect('/admin/')

        if request.user.groups.filter(name='Medico').exists():
            return redirect('proc_menu_alias')
        elif request.user.groups.filter(name='Funcionario').exists():
            return render(request, 'myapp/func_menu.html')
        elif request.user.groups.filter(name='Paciente').exists():
            return redirect('procedimento_list_alias')
    else:
        return render(request, 'index.html')

# Listagem de procedimentos
class procedimento_list(SingleTableView):
    from .tables import procedimento_table
    model = Procedimento
    table_class = procedimento_table
    template_name = 'myapp/procedimento_list.html'


# Criação de procedimentos (restrito a funcionários e administradores)
class procedimento_create(AdminOrFuncionarioOrMedicoRequiredMixin, CreateView):
    model = Procedimento
    fields = ['nome', 'paciente', 'medico', 'data', 'descricao']

    def get_success_url(self):
        return reverse_lazy('proc_menu_alias')


# Atualização de procedimentos (restrito a funcionários e administradores)
class procedimento_update(AdminOrFuncionarioOrMedicoRequiredMixin, UpdateView):
    model = Procedimento
    fields = ['nome', 'paciente', 'medico', 'data', 'descricao']

    def get_success_url(self):
        return reverse_lazy('proc_menu_alias')


# Exclusão de procedimentos (restrito a funcionários e administradores)
class procedimento_delete(AdminOrFuncionarioRequiredMixin, DeleteView):
    model = Procedimento
    template_name_suffix = '_delete'

    def get_success_url(self):
        return reverse_lazy('proc_menu_alias')


# Menu de procedimentos
class procedimento_menu(SingleTableView):
    from .tables import procedimento_table
    model = Procedimento
    table_class = procedimento_table
    template_name_suffix = '_menu'
    table_pagination = {"per_page": 10}
    template_name = 'myapp/proc_menu.html'


# Formulário customizado para criação de usuários
class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="Grupo")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'group']

    def save(self, commit=True):
        user = super().save(commit=False)
        group = self.cleaned_data['group']
        if commit:
            user.save()
            user.groups.add(group)
        return user


# Listagem dos usuários
class UserListView(AdminOrFuncionarioRequiredMixin, SingleTableView):
    from .pessoas import UserTable
    model = User
    table_class = UserTable
    template_name = 'myapp/user_menu.html'


# Criação de usuários
class UserCreateView(AdminOrFuncionarioRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('user_menu_alias')


# Edição de usuários
class UserUpdateView(AdminOrFuncionarioRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'groups']
    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('user_menu_alias')
    


# Exclusão de usuários
class UserDeleteView(AdminOrFuncionarioRequiredMixin, DeleteView):
    model = User
    template_name_suffix = '_delete'
    success_url = reverse_lazy('user_menu_alias')