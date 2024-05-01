from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
import mysql.connector

# Create your views here.
def home(request):
    return render(request,'home.html')

# Inserção dos dados dos usuários no banco 
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'login.html', data)


# Formulário do painel de login
def painel(request):
    return render(request,'login.html')


# Processa o login 
def dologin(request): 
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/home/') # Retorna a URL homne
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'login.html', data)


# Página inicial do dashboard
def dashboard(request):
    return render(request,'dashboard/home.html') # Retorna a página home 


# Logout do sistema 
def logouts(request):
    logout(request)
    return redirect('/Login/')


# Painel de redefinição de senha
def AlterarSenha(request):
    return render(request, 'AlterarSenha.html')

#=================================================================================================
# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    database='sushihashi',
)
cursor = conexao.cursor()


def LerDB(email=None):
    comando = 'SELECT * FROM auth_user WHERE username = %s'
    params = (email,)
    try:
        cursor.execute(comando, params)
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        return None

def Atualizacao(email, senha):
    senha_criptografada = make_password(senha)
    comando = 'UPDATE auth_user SET password = %s WHERE username = %s'
    params = (senha_criptografada, email)
    try:
        cursor.execute(comando, params)
        conexao.commit()
        return True
    except Exception as e:
        print(f'Ocorreu um erro ao atualizar a senha: {e}')
        conexao.rollback()
        return False

def changePassword(request):
    data = {}
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        confirm_password = request.POST.get('newpassword-conf')
        email = request.POST.get('email')

        if new_password != confirm_password:
            data['msg'] = 'Senha e confirmação de senha diferentes!'
            data['class'] = 'alert-danger'
            return render(request, 'AlterarSenha.html', data)
        resultados = LerDB(email=email)
        print(resultados) 
        if not resultados:
            data['msg'] = 'Seu e-mail está incorreto!'
            data['class'] = 'alert-danger'
        else:
            # Realiza a atualização da senha no banco de dados
            if Atualizacao(email=email, senha=new_password):
                data['msg'] = 'Senha atualizada com sucesso!'
                data['class'] = 'alert-success'
            else:
                data['msg'] = 'Ocorreu um erro ao atualizar a senha. Por favor, tente novamente.'
                data['class'] = 'alert-danger'

    return render(request, 'AlterarSenha.html', data)



#=================================================================================================
# ChangePassword do Django
    # data = {}
    # if(request.POST['newpassword'] != request.POST['newpassword-conf']):
    #     data['msg'] = 'Senha e confirmação de senha diferentes!'
    #     data['class'] = 'alert-danger'
    #     return render(request, 'AlterarSenha.html', data)
    # else:
    #     user = User.objects.get(username=request.user.username)
    #     user.set_password(request.POST['newpassword'])
    #     user.save()
    #     data['msg'] = 'Senha alterada com sucesso!'
    #     data['class'] = 'alert-success'
    #     logout(request)
    #     return redirect('/Login/', data)
    

# Catalógo de Produtos 
def Catalogo(request):
    return render(request, 'dashboard/catalogo.html')


# Sobre o site 
def sobreNos(request):
    return render(request, 'dashboard/sobreNos.html')

# Carrinho de Compras 
def carrinho(request):
    return render(request, 'dashboard/carrinho.html')

# Pesquisa de satisfação do site 
def pesquisa(request):
    return render(request, 'dashboard/pesquisa.html')
