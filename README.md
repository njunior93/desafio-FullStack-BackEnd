# 🚀 API - Sistema de Gerenciamento de Voluntários

Backend desenvolvido com **FastAPI** para gerenciamento de voluntários.

Esta API permite:

- ✅ Cadastrar voluntários
- ✅ Listar voluntários
- ✅ Editar voluntários
- ✅ Filtrar voluntários
- ✅ Inativar voluntários (Soft Delete)

---

# 🛠️ Tecnologias Utilizadas

<div align="left">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge)
![Uvicorn](https://img.shields.io/badge/Uvicorn-111111?style=for-the-badge)

</div>

---

# 📌 Funcionalidades

## 👨‍💻 CRUD Completo

- ➕ Criar voluntário
- 📋 Listar voluntários
- ✏️ Editar voluntário
- ❌ Inativar voluntário

---

# 📌 Repositorio FrontEnd


([📁 Repositório FrontEnd](https://github.com/njunior93/desafio_fullStack.git))

---

# ⚙️ Como Rodar o Projeto

## 📥 Clone o repositório

```bash
git clone https://github.com/njunior93/desafio_fullStack.git
```

---

# 🐍 Criar ambiente virtual

```bash
python -m venv venv
```

---

# ▶️ Ativar ambiente virtual

## Windows

```bash
venv\Scripts\activate
```

## Linux / MacOS

```bash
source venv/bin/activate
```

---

# 📦 Instalar dependências

```bash
pip install -r requirements.txt
```

---

# 🚀 Rodar aplicação

```bash
uvicorn app.main:app --reload
```

Servidor disponível em:

```bash
http://localhost:8000
```

---

# 📄 Documentação Automática da API

FastAPI gera documentação automaticamente.

## Swagger UI

```bash
http://localhost:8000/docs
```

## ReDoc

```bash
http://localhost:8000/redoc
```

---

# 🔗 Endpoints

## 📋 Listar voluntários

```http
GET /voluntarios
```

---

## 🔍 Buscar voluntário por ID

```http
GET /voluntarios/{id}
```

---

## ➕ Criar voluntário

```http
POST /voluntarios
```

---

## ✏️ Atualizar voluntário

```http
PUT /voluntarios/{id}
```

---

## ❌ Inativar voluntário (Soft Delete)

```http
DELETE /voluntarios/{id}
```

---

# 🧠 Decisões Técnicas

## ✅ FastAPI

Utilizado pela alta performance, tipagem forte e documentação automática.

---

## ✅ SQLAlchemy

Utilizado como ORM para manipulação do banco de dados.

---

## ✅ SQLite

Banco leve e simples para facilitar execução local do desafio técnico.

---

## ✅ Soft Delete

A exclusão de voluntários foi implementada utilizando alteração de status ao invés de remoção definitiva do banco.

---

# 📌 Regras de Negócio

- Nome obrigatório
- Email obrigatório
- Telefone obrigatório
- Cargo obrigatório
- Não permitir emails duplicados
- Status ativo/inativo
- Data de cadastro automática

---

# 🧪 Testes

Exemplos de testes previstos:

```python
test("deve criar voluntário com dados válidos")
test("não deve permitir email duplicado")
```

---

# 🌐 Integração com Frontend

A API foi desenvolvida para integração com frontend em:

- React
- Vite
- TypeScript
- TanStack Query

---

# 📁 Variáveis de Ambiente

Atualmente o projeto não necessita de variáveis sensíveis.

---

# 👨‍💻 Autor

Feito por **Natanael Junior**

🔗 GitHub:
https://github.com/njunior93

---

# ⭐ Observações

Projeto desenvolvido como desafio técnico Fullstack utilizando FastAPI + React.

Foco principal:

- organização
- componentização
- boas práticas
- integração frontend/backend
- experiência do usuário
