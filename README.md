# LivrariaIGE

## O sistema
A Livraria IGE é um software para consultas de livros, baseado nos cursos do Instituto de Geologia e Engenharias, campus II da UNIFESSPA - Marabá

O sistema permite que os usuários se registrem, pesquisem livros disponíveis, realizem comentários sobre os livros, favoritem suas obras preferidas e gerenciem sua lista de favoritos. Além disso, a plataforma oferece um ambiente intuitivo e organizado, possibilitando uma melhor experiência na busca e administração dos materiais acadêmicos.

O objetivo principal da Livraria IGE é centralizar e disponibilizar informações de maneira eficiente para estudantes e professores, promovendo um ambiente colaborativo onde os usuários podem interagir e compartilhar suas opiniões sobre as obras cadastradas. No futuro, o sistema pode incluir novas funcionalidades, como sugestões personalizadas e categorização avançada de livros.

## Iniciação do Projeto

### Windows:
1. Ao descompactar a pasta, abra o cmd/terminal e execute os seguintes comandos:
   ```sh
   pip install virtualenv
   python -m venv venv
   cd venv\Scripts
   activate
   cd ..\..
   ```

### Linux:
1. Execute os seguintes comandos:
   ```sh
   pip3 install virtualenv
   pip3 -m venv venv
   source myvenv/bin/activate
   ```

* Se houver problemas com o `pip`, instale manualmente:
  - **Windows**: `python get-pip.py`
  - **Linux**: `sudo apt install python3-pip`

**Mantenha o terminal aberto, pois ele estará com o ambiente virtual ativado.**

## Instalação de Dependências
Com o ambiente virtual ativado, instale os requisitos do projeto:
- **Windows**: `pip install -r requirements.txt`
- **Linux**: `pip3 install -r requirements.txt`

## Configuração do Banco de Dados (MySQL)
Crie o banco de dados e o usuário para a aplicação:
```sql
CREATE DATABASE LivrariaIGE;
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON LivrariaIGE . * TO 'admin'@'localhost';
FLUSH PRIVILEGES;
```

## Migração do Banco de Dados
No terminal (IDE ou CMD), execute os seguintes comandos:
- **Windows:**
  ```sh
  python manage.py makemigrations
  python manage.py migrate
  ```
- **Linux:**
  ```sh
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

## Criação do Super Usuário
Crie um super usuário para gerenciar o sistema:
- **Windows:** `python manage.py createsuperuser`
- **Linux:** `python3 manage.py createsuperuser`

Preencha os campos conforme necessário. O email é opcional.

## Executando o Servidor
Para rodar o servidor, utilize um dos seguintes comandos:
- **Windows:** `python manage.py runserver`
- **Linux:** `python3 manage.py runserver`

A aplicação estará acessível em `127.0.0.1:8000` ou `localhost:8000`.

Para encerrar o servidor, use `CTRL + C` no terminal.

## URLs da Aplicação
| Rota | Descrição |
|------|----------|
| `/` | Página inicial |
| `/admin` | Sistema de administração (CRUD de dados) |
| `/autor/<slug:slug>` | Perfil de um autor |
| `/livros/` | Lista de livros |
| `/livros/<slug:slug>` | Detalhes de um livro específico |
| `/livros/adicionar/` | Adicionar um livro (somente professores) |
| `/livros/<slug:slug>/favoritar/` | Favoritar um livro (em desenvolvimento) |
| `/livros/<slug:slug>/desfavoritar/` | Desfavoritar um livro (em desenvolvimento) |
| `/registrar/` | Registrar um novo usuário |
| `/login/` | Realizar login |
| `/logout/` | Logout (não funcional manualmente) |
| `/perfil/<username>` | Perfil de um usuário |