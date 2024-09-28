from django.shortcuts import render, redirect
from .models import Usuario  # Importa o modelo Usuario
from django.contrib.auth import authenticate, login  # Importa funções de autenticação

# View para renderizar a página inicial
def home(request):
    return render(request, 'usuarios/home.html')

# View para gerenciar a criação e listagem de usuários
def usuarios(request):
    if request.method == 'POST':
        # Coleta os dados enviados pelo formulário
        novo_usuario = Usuario()  # Cria uma nova instância de Usuario
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.senha = request.POST.get('senha')  # ATENÇÃO: não é seguro armazenar senhas em texto claro
        novo_usuario.email = request.POST.get('email')
        novo_usuario.telefone = request.POST.get('telefone')

        # Salva o novo usuário no banco de dados
        novo_usuario.save()

    # Coleta todos os usuários cadastrados para exibir na página
    usuarios = {
        'usuarios': Usuario.objects.all()  # Recupera todos os usuários do banco de dados
    }

    # Renderiza a página de login após o cadastro
    return render(request, 'usuarios/login.html', usuarios)

# View para realizar o login
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        user = authenticate(request, email=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('pagina_inicial', usuario_id=user.id)  # Passa o ID do usuário para a próxima página

        return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'login.html')

# View para o cadastro de um novo usuário
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        senha = request.POST['senha']
        email = request.POST['email']
        telefone = request.POST['telefone']
        descricao = request.POST['descricao']  # Captura a descrição

        novo_usuario = Usuario.objects.create(
            nome=nome,
            senha=senha,
            email=email,
            telefone=telefone,
            descricao=descricao  # Salva a descrição
        )
        novo_usuario.save()

        return redirect('login')

    return render(request, 'cadastro.html')

def pagina_inicial(request, usuario_id):
    usuario = Usuario.objects.get(id_usuario=usuario_id)  # Busca o usuário pelo ID
    return render(request, 'pagina_inicial.html', {'usuario': usuario})

