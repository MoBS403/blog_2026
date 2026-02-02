# Projeto Blog Django

Um **blog completo desenvolvido em Django** com MySQL, permitindo a criação e gerenciamento de posts, categorias e comentários.  
O projeto é modular, seguro e estilizado com **Bootstrap 4** e **Crispy Forms**, incluindo editor WYSIWYG para conteúdo.

---

## 🧰 Tecnologias e Bibliotecas

- **Framework:** Django
- **Banco de Dados:** MySQL
- **Linguagens:** Python, HTML, CSS, JavaScript

### Apps do projeto
- `posts` – Gerenciamento de postagens
- `categorias` – Organização por categorias
- `comentarios` – Sistema de comentários

### Django core apps
- `django.contrib.admin` – Painel administrativo
- `django.contrib.auth` – Sistema de autenticação
- `django.contrib.contenttypes`
- `django.contrib.sessions`
- `django.contrib.messages`
- `django.contrib.staticfiles`
- `django.contrib.humanize` – Formatação de datas, números e moedas

### Terceiros
- `crispy_forms` – Formulários estilizados
- `crispy_bootstrap4` – Integração com Bootstrap 4
- `axes` – Segurança e prevenção de login suspeito
- `django_summernote` – Editor de texto rico (WYSIWYG)

---
### Configurar banco de dados MySQL

No arquivo settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### Executar migrations

python manage.py migrate

### Criar superusuário

python manage.py createsuperuser

### Executar servidor

python manage.py runserver

### 📝 Funcionalidades

Posts: Criar, editar e excluir postagens

Categorias: Organizar posts por categorias

Comentários: Sistema de comentários com moderação

Editor WYSIWYG: Criar conteúdo com formatação avançada usando Django Summernote

Autenticação: Cadastro, login e logout de usuários

Segurança: Proteção contra tentativas de login suspeitas com axes

Formulários bonitos: Utilizando Crispy Forms e Bootstrap 4


### 📸 Demonstração

Adicione aqui prints ou GIFs do seu projeto (ex.: página inicial, post, painel admin, etc.)

###💡 Observações

django.contrib.humanize é utilizado para exibir datas e números de forma amigável.

Crispy Forms e Bootstrap 4 melhoram a aparência dos formulários.

Axes aumenta a segurança de login.

Django Summernote fornece editor WYSIWYG para posts e comentários.

### 📚 Links Úteis

Django Documentation - >  https://docs.djangoproject.com/en/6.0/
Django Crispy Forms  - >  https://django-crispy-forms.readthedocs.io/en/latest/
Django Summernote    - >  https://github.com/lqez/django-summernote
Axes Documentation   - >  https://django-axes.readthedocs.io/en/latest/



