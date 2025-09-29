# 🐾 LaudosVet: Sistema de Cadastro de Laudos Veterinários
Este projeto é uma API RESTful desenvolvida em Python (Flask + SQLAlchemy) para gerenciar o cadastro de pets e seus respectivos tutores, início de um projeto maior que será continuado com o objetivo final de desenvolver um sistema de cadastro de laudos.

Ele faz parte do MVP da disciplina **Desenvolvimento Full Stack Básico**.

Neste primeiro momento, a API oferece endpoints para as operações CRUD (Criar, Ler, Atualizar e Deletar) essenciais para o gerenciamento de dados de tutores e seus pets..

## 🛠️ Como Executar (Instalação e Configuração)

Siga os passos abaixo para configurar e iniciar o servidor da API no seu ambiente local.

### 1. Clonagem e Configuração do Ambiente

Primeiro, clone este repositório e navegue até o diretório raiz.

**Recomendação:** É fortemente indicado o uso de ambientes virtuais (como `venv` ou `virtualenv`) para isolar as dependências do projeto.

# 1. Cria o ambiente virtual (se necessário)
python -m venv venv

# 2. Ativa o ambiente virtual
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

#### Execute o comando a seguir para instalar as dependendências necessárias para executar este projeto:
pip install -r requirements.txt

##### Inicie o servidor:
O servidor pode ser iniciado com o comando 'flask run'. Após a inicialização, a API estará acessível em http://localhost:5000

⚙️ Endpoints Principais
Recurso	Método	Descrição
/tutor	POST	Cadastra um novo tutor.
/tutores	GET	Lista todos os tutores cadastrados.
/pet	POST	Cadastra um novo pet (requer o id do tutor).
/pets	GET	Lista todos os pets cadastrados.
/pet?id=<id>	DELETE	Remove um pet pelo seu ID.