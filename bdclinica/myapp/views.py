from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Procedimento
from django.views.generic import CreateView, ListView, UpdateView , DeleteView
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, Group 

def index(request):
    
    usuario = request.POST.get('username')
    senha = request.POST.get('password')
    user = authenticate(username=usuario, password=senha)
    if (user is not None):
        login(request, user)
        request.session['username'] = usuario
        request.session['password'] = senha
        request.session['usernamefull'] = user.get_full_name()

         # Redireciona para o Django Admin se o usuário for um superusuário
        if user.is_superuser:
            return redirect('admin/')
            #return HttpResponse("toaqui")
        
        #print(request.session['username'])
        #print(request.session['password'])
        #print(request.session['usernamefull'])

        if request.user.groups.filter(name='Medico').exists():
            return redirect('proc_menu_alias')
        elif request.user.groups.filter(name='Funcionario').exists():
            return render(request, 'myapp/func_menu.html')
        elif request.user.groups.filter(name='Paciente').exists():
            return redirect('procedimento_list_alias') 
    else:
        print("coiso")
        return render(request, 'index.html')

def pagina1(request):
    return render(request, 'pagina1.html')

def pagina2(request):
    from .models import Procedimento
    dicionario = {}
    registros = Procedimento.objects.all()
    dicionario['Procedimentos'] = registros
    return render(request, 'pagina2.html', dicionario)

def pagina3(request):
    from .models import Procedimento
    dicionario = {}
    registros = Procedimento.objects.all()
    dicionario['Procedimentos'] = registros
    return render(request, 'pagina3.html', dicionario)

class procedimento_list(ListView):
    from .models import Procedimento
    model = Procedimento

class procedimento_create(CreateView):
    from .models import Procedimento
    model = Procedimento
    fields = ['nome', 'paciente', 'medico', 'data', 'descricao']
    def get_success_url(self):
        return reverse_lazy('proc_menu_alias')

class procedimento_update(UpdateView):
    from .models import Procedimento
    model = Procedimento
    fields = ['nome', 'paciente', 'medico', 'data', 'descricao']
    def get_success_url(self):
        return reverse_lazy('proc_menu_alias')


class procedimento_delete(DeleteView):
    from .models import Procedimento
    model = Procedimento
    fields = ['nome', 'paciente', 'medico', 'data', 'descricao']
    template_name_suffix = '_delete'
    def get_success_url(self):
        return reverse_lazy('proc_menu_alias')

class procedimento_menu(SingleTableView):
    from .models import Procedimento
    from .tables import procedimento_table
    model = Procedimento
    table_class = procedimento_table
    template_name_suffix = '_menu'
    table_pagination = {"per_page": 5}
    template_name = 'myapp/proc_menu.html'

class CustomUserCreationForm(UserCreationForm):
    from django.contrib.auth.models import User, Group 
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="Grupo")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'group']

    def save(self, commit=True):
        user = super().save(commit=False)
        group = self.cleaned_data['group']
        if commit:
            user.save()
            user.groups.add(group)  # Adicionar o usuário ao grupo selecionado
        return user

# Listagem dos usuários
class UserListView(SingleTableView):
    from django.contrib.auth.models import User, Group
    from .pessoas import UserTable    
    model = User
    table_class = UserTable
    template_name = 'myapp/user_menu.html'

# Criar usuário
class UserCreateView(CreateView):
    from django.contrib.auth.models import User, Group
    model = User
    form_class = CustomUserCreationForm
    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('user_menu_alias')

# Editar usuário (com opção de editar o grupo)
class UserUpdateView(UpdateView):
    from django.contrib.auth.models import User, Group
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'groups']
    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('user_menu_alias')

# Deletar usuário
class UserDeleteView(DeleteView):
    from django.contrib.auth.models import User, Group
    model = User
    template_name_suffix = '_delete'
    success_url = reverse_lazy('user_menu_alias')