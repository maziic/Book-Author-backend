# react-django-books-author-app-beckend

A Book storing platform with Users Login & JWt Authentication

## Table of Contents

- [Technologies](#Technologies)
- [Setting up the backend server](#Setting-up-the-backend-server)
- [Credits](#credits)

## Technologies

1. React
2. Tailwind CSS
3. Django REST Framework

## Setting up the backend server

1. Clone the project

```bash
git clone https://github.com/maziic/Book-Author-backend.git
```

2. Go to the project directory (backend)

```bash
cd backend
```

3. Create a virtual environment and activate it (Windows)

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Migrate

```bash
python manage.py migrate
```

6. Create admin/superuser

```bash
python manage.py createsuperuser
```

7. Finally run the project

```bash
python manage.py runserver
```

Now the project should be running on http://localhost:8000/

## Credits

Developer : [Neaz Mahmud](https://github.com/maziic)
