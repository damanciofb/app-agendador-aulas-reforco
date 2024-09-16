# APP Reforço Escolar

Um sistema web moderno e simples para gerenciar alunos e seus horários de reforço escolar, oferecendo uma interface intuitiva para cadastro, visualização e exportação dos dados.

## 📋 Funcionalidades

- Cadastro de alunos com dados como nome, idade, série e matérias de reforço.
- Visualização de agendamentos de aulas por aluno ou para todos.
- Exportação dos dados para Excel (individual ou em massa).
- Interface responsiva e moderna.
  
## 🖼️ Capturas de Tela

> Insira aqui capturas de tela ou GIFs do seu sistema para dar uma ideia visual do projeto.

| Página Inicial                              | Cadastro de Aluno                           | Visualização de Agendamentos                 |
|---------------------------------------------|---------------------------------------------|---------------------------------------------|
| ![Home](link_para_imagem_home)              | ![Cadastro](link_para_imagem_cadastro)      | ![Agendamentos](link_para_imagem_agendamentos) |

## 🚀 Tecnologias Utilizadas

- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS3
- **Banco de Dados**: MongoDB
- **Servidores**: Nginx, Gunicorn
- **Ferramentas de Exportação**: Pandas (para exportação de dados para Excel)
  
## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.x instalado
- MongoDB configurado
- Servidor Linux (preferencialmente Ubuntu 24.04)

### Passos para rodar o projeto localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/damanciofb/app-agendador-aulas-reforco.git

2. Acesse o diretório do projeto:

   ```bash
   git clone https://github.com/damanciofb/app-agendador-aulas-reforco.git

3. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate

4. Instale as dependências:
  
   ```bash
   pip install Flask Flask-PyMongo pandas openpyxl gunicorn python-dotenv dnspython Werkzeug Jinja2 MarkupSafe itsdangerous click

5. Estrutura de diretorios

  ````bash
  meu_projeto_reforco 
  ├── app.py
  ├── static
  │   ├── js
  │   │   └── script.js
  │   └── style.css
  └── templates
      ├── base.html
      ├── index.html
      ├── register.html
      ├── schedule.html
      └── success.html
````
### Instalação do MongoDB

1. Atualizar o sistema
   
  ````bash
  sudo apt update
  sudo apt upgrade
  ````
2. Importar a chave GPG do MongoDB
  
  ````bash
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo tee /etc/apt/trusted.gpg.d/mongodb-server-6.0.asc
  ````
3. Adicionar o repositório oficial do MongoDB

  ````bash
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
  ````
4. Instalar o MongoDB

  ````bash
sudo apt update
sudo apt install -y mongodb-org
  ````  

5. Iniciar serviço

  ````bash
sudo systemctl start mongod
  ````
6. Habilitar MongoDB na inicialização do sistema

  ````bash
sudo systemctl enable mongod
  ````
7. Acessando o shell do MongoDB

  ````bash
  mongosh
  ````
8. Criar o Bando de dados

  ````bash
  use alunos
  use agenda
  ````
9. Lista bancos criados

  ````bash
  show dbs
  ````

Após adicionar todos os arquivos em seus respequitivos diretorios.

