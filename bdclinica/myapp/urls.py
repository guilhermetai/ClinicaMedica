from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_alias'),
    path('proc_menu', views.procedimento_menu.as_view(), name='proc_menu_alias'),
    path('procedimento_list/', views.procedimento_list.as_view(), name='procedimento_list_alias'),
    path('procedimento_create/', views.procedimento_create.as_view(), name='procedimento_create_alias'),
    path('procedimento_update/<int:pk>/', views.procedimento_update.as_view(), name='procedimento_update_alias'),
    path('procedimento_delete/<int:pk>/', views.procedimento_delete.as_view(), name='procedimento_delete_alias'),
    path('users_menu', views.UserListView.as_view(), name='user_menu_alias'),
    path('users_create/', views.UserCreateView2.as_view(), name='user_create_alias'),
    path('users_update/<int:pk>', views.UserUpdateView.as_view(), name='user_update_alias'),
    path('users_delete/<int:pk>', views.UserDeleteView.as_view(), name='user_delete_alias'),
    path('alterar_senha/<int:pk>',views.ChangePasswordUser.as_view(), name='alterar_senha_alias'),
]