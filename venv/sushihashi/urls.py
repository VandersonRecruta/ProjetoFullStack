"""
URL configuration for sushihashi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios.views import home, store, painel, dologin, dashboard, logouts, AlterarSenha, changePassword, Catalogo, sobreNos, carrinho, pesquisa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('Login/', painel), # Chama a função painel
    path('store/', store), # Chama a função store
    path('login/', dologin), # Chama a função dologin 
    path('logout/', logouts), # Chama a função logouts
    path('AlterarSenha/', AlterarSenha), # Chama a função AlterarSenha
    path('NovaSenha/', changePassword), # Chama a função changePassword 
    path('home/', dashboard), # Chama a função dashboard
    path('catalogo/', Catalogo), # Chama a função dashboard
    path('sobreNos/', sobreNos), # Chama a função dashboard
    path('carrinho/', carrinho), # Chama a função dashboard
    path('pesquisa/', pesquisa), # Chama a função dashboard
]
