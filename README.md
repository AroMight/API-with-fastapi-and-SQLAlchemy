# Projeto FastAPI + SQLAlchemy + Alembic + Docker + PostgreSQL

Este é um pequeno protótipo de uma aplicação utilizando FastAPI, SQLAlchemy, Alembic, Docker e PostgreSQL. Este projeto serve como base para um projeto maior que está sendo desenvolvido.

## Pré-requisitos

Certifique-se de ter instalado:

- Docker
- Docker Compose

## Como usar

1. **Clonar o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
2. **Configurar o ambiente:**

  Crie um arquivo `.env` na raiz do projeto com base no `.env.example`. Preencha as variáveis de ambiente necessárias, como as credenciais do banco de dados.

3. **Subir os serviços:**

    ```bash
    docker-compose up -d --build
Isso irá construir e iniciar os containers do Docker para a aplicação e o banco de dados.

4. **Executar as migrações do banco de dados:**

    ```bash
    docker-compose exec web alembic upgrade head
Isso aplicará todas as migrações pendentes ao banco de dados.

5. **Acessar a aplicação:**

Acesse a API através de:

    http://localhost:8000

## Estrutura do projeto

- **app/**: Contém o código da aplicação FastAPI.
- **alembic/**: Contém as migrações do banco de dados gerenciadas pelo Alembic.
- **docker-compose.yml**: Define os serviços Docker necessários para a aplicação.
- **Dockerfile**: Configura o ambiente Docker para a aplicação.
- **.env.example**: Exemplo de arquivo de variáveis de ambiente. Renomeie para `.env` e configure conforme necessário.
- **README.md**: Este arquivo.
  
## Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Abra um pull request com suas alterações.
