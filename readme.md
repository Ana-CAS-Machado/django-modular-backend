# Django Modular Backend

## Requisitos

- Python 3.10+
- pip

## Passos para rodar o projeto

### 1. Crie e ative o ambiente virtual

No terminal, dentro da pasta `backend`:

**Windows:**
```sh
python -m venv env
env\Scripts\activate
```

**Linux/Mac:**
```sh
python3 -m venv env
source env/bin/activate
```

### 2. Instale as dependências

```sh
pip install django
pip install djangorestframework
pip install django-ninja
pip install django-ninja-extra
```

### 3. (Opcional) Gere o arquivo requirements.txt

```sh
pip freeze > requirements.txt
```

### 4. Configure o banco de dados

Crie as tabelas do banco de dados:

```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário

```sh
python manage.py createsuperuser
```

### 6. Rode o servidor de desenvolvimento

```sh
python manage.py runserver
```

---

## Acessos

- Admin: http://localhost:8000/admin/
- API Ninja: http://localhost:8000/api/docs

---

## Dependências principais

- django
- djangorestframework
- django-ninja
- django-ninja-extra

---

**Dica:**  
Sempre ative o ambiente virtual antes de rodar comandos do projeto!