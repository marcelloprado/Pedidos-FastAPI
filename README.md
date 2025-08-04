# 🚀 FastAPI - Sistema de Pedidos

Este é um projeto desenvolvido com **FastAPI**, como parte do curso da **Hashtag Treinamentos**, com objetivo de aplicar conceitos de criação de APIs modernas e seguras. O sistema permite autenticação de usuários e gerenciamento completo de pedidos.

> Projeto desenvolvido por **Marcello Prado Muller**.

🔗 Repositório: [github.com/marcelloprado/Pedidos-FastAPI](https://github.com/marcelloprado/Pedidos-FastAPI.git)

---

## 📸 Demonstração

<p align="center">
  <img src="caminho/para/screenshot1.png" width="600">
  <br>
  <img src="caminho/para/screenshot2.png" width="600">
</p>

---

## 📚 Funcionalidades

### 🔐 Autenticação (`/auth`)
- `POST /auth/criar_conta` – Criar nova conta de usuário
- `POST /auth/login` – Login via JSON
- `POST /auth/login-form` – Login via formulário
- `GET /auth/refresh` – Atualizar token de acesso

### 📦 Pedidos (`/pedidos`)
- `GET /pedidos/` – Visualizar pedidos do usuário
- `POST /pedidos/pedido` – Criar novo pedido
- `POST /pedidos/pedido/cancelar/{id_pedido}` – Cancelar pedido
- `POST /pedidos/pedido/adicionar_item/{id_pedido}` – Adicionar item ao pedido
- `POST /pedidos/pedido/remover-item/{id_item_pedido}` – Remover item do pedido
- `POST /pedidos/pedido/finalizar/{id_pedido}` – Finalizar pedido
- `GET /pedidos/pedido/{id_pedido}` – Visualizar pedido específico
- `GET /pedidos/listar/pedidos-usuario` – Listar todos os pedidos do usuário

---

## 🔐 Autenticação

O projeto utiliza **JWT Token** para proteger as rotas. Você pode autenticar via Swagger usando o botão `Authorize`.

---

## 🚧 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) – Migrações
- [Python-Jose](https://python-jose.readthedocs.io/) – JWT
- [SQLite](https://www.sqlite.org/index.html) – Banco de dados leve

---

## ▶️ Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/marcelloprado/Pedidos-FastAPI.git
   cd Pedidos-FastAPI
   
2. Crie e ative um ambiente virtual:
    ```bash
     python -m venv venv
     source venv/bin/activate  # Linux/macOS
     venv\Scripts\activate     # Windows
   

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Execute as migrações para criar o banco:
    ```bash
     alembic upgrade head 

5. Rode o servidor:
    ```bash
     uvicorn main:app --reload
 
6. Acesse a documentação Swagger:
     ```bash
    http://localhost:8000/docs

## 🧪 Testes
  Você pode testar a API via Swagger, Postman ou Insomnia.
  
---

## 📂 Estrutura do Projeto

  📁 ProjetoFastAPI/ <br>
 ┣ 📄 main.py <br>
 ┣ 📄 models.py <br>
 ┣ 📄 schemas.py <br>
 ┣ 📄 auth_routes.py <br>
 ┣ 📄 order_routes.py <br>
 ┣ 📄 dependencies.py <br>
 ┣ 📄 alembic.ini <br>
 ┣ 📁 alembic/ <br>
 ┣ 📁 venv/ <br>
 ┣ 📄 banco.db (ignorado) <br>
 ┣ 📄 .env (ignorado) <br>
 ┣ 📄 requirements.txt <br>
 ┣ 📄 testes.py <br>
 ┗ 📄 .gitignore <br>

### 🎓 Projeto desenvolvido por Marcello Prado Muller
### 📘 Curso: Hashtag Treinamentos - FastAPI
