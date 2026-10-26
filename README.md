# Circuito Terê-Verde — Guia prático de parques e trilhas de Teresópolis-RJ

MVP de back-end desenvolvido para o curso de Análise e Desenvolvimento de Sistemas da UNIFESO, em Teresópolis, RJ.

A API disponibiliza informações sobre parques da região e suas atrações e trilhas relacionadas para consumo por um front-end.

## Funcionalidades

- Modelos Django para parques, atrações e trilhas, com relacionamentos entre eles.
- API REST feita com Django REST Framework:
  - listagem de parques;
  - consulta de um parque pelo slug;
  - inclusão de atrações e trilhas relacionadas nas respostas dos parques.
- Cadastro e gerenciamento dos dados pelo Django Admin.
- Upload de imagens dos parques.
- SQLite como banco de dados padrão.

> Este repositório contém o back-end. As páginas visuais do front-end são implementadas em um projeto separado.

## Tecnologias

- Python
- Django
- Django REST Framework
- SQLite
- Pillow (suporte a imagens)

## Executar localmente

### Pré-requisitos

- Git
- Python compatível com as versões das dependências declaradas em [`requirements.txt`](requirements.txt)

### 1. Clonar o repositório

```bash
git clone https://github.com/samuelmedeiros123/back-end-circuito-tere-verde>
cd <PASTA_DO_REPOSITORIO> 
```

### 2. Criar e ativar um ambiente virtual

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Criar as tabelas do banco

```bash
python manage.py migrate
```

O projeto usa SQLite por padrão. Em uma instalação nova, as migrações criam um banco local (`db.sqlite3`).

### 5. Criar um usuário administrador

```bash
python manage.py createsuperuser
```

Siga as instruções para cadastrar o usuário e a senha do Django Admin.

### 6. Iniciar o servidor

```bash
python manage.py runserver
```

O servidor local ficará em `http://127.0.0.1:8000/`.

### 7. Cadastrar parques, atrações e trilhas

Abra `http://127.0.0.1:8000/admin/` e entre com o superusuário criado. Cadastre os parques e depois as atrações e trilhas, associando cada registro ao parque correspondente.

Em uma instalação nova, as tabelas começam vazias. O banco local e as imagens de mídia não são incluídos no Git, então precisam ser cadastrados/adicionados em cada ambiente.

## Endpoints

Todas as rotas da API usam o prefixo `/api/v1/`.

| Método | Endpoint | Descrição |
| --- | --- | --- |
| `GET` | `/api/v1/parquesteresopolis/` | Lista os parques |
| `GET` | `/api/v1/parquesdetalhes/<slug>/` | Consulta um parque pelo slug |

Exemplo de consulta de detalhe:

```text
http://127.0.0.1:8000/api/v1/parquesdetalhes/parque-nacional-da-serra-dos-orgaos-parnaso/
```

As respostas incluem os campos do parque e as listas `atrações` e `trilhas`. Se não houver registros relacionados, essas listas serão vazias (`[]`).

O campo `image` contém o caminho da imagem. Durante o desenvolvimento, arquivos de mídia são servidos sob `/media/`, por exemplo:

```text
http://127.0.0.1:8000/media/parques/nome-da-imagem.webp
```

## Estrutura do projeto

```text
api/             Views, serializers e rotas da API
mvpbackend/      Configurações e rotas principais do Django
parquestere/     Modelos, Admin e migrações
media/           Arquivos de imagem usados localmente
manage.py        Utilitário de administração do Django
requirements.txt Dependências Python do projeto
```

## Observações

- O arquivo `db.sqlite3` e a pasta `media/` são ignorados pelo Git.

## Integrantes

- Samuel Medeiros
- Renan Garcia
- Silas Junior
- Davi Soares
- Rodrigo Campos
- Rick
