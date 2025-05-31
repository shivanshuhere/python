
# 📘 Django

## 🧠 What is Django?
- Django is a **high-level Python web framework**.
- It helps in building **secure**, **scalable**, and **maintainable** websites quickly.
- Follows the **MVT (Model-View-Template)** architecture.

## 🔧 Django Installation

```bash
pip install django
```

Create a new project:

```bash
django-admin startproject project_name
cd project_name
python manage.py runserver
```

## 🗂 Django Project Structure

```
project_name/
│
├── manage.py           # Command-line utility
├── project_name/
│   ├── __init__.py
│   ├── settings.py     # Project settings
│   ├── urls.py         # Main URL routing
│   └── wsgi.py
```

## 📦 Creating an App

```bash
python manage.py startapp app_name
```

Add the app in `settings.py`:

```python
INSTALLED_APPS = [
    'app_name',
]
```

## 🌐 URL Routing

In `app_name/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

In `project_name/urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    path('', include('app_name.urls')),
]
```

## 🖼 Views and Templates

**views.py:**

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

**home.html (inside templates/ folder):**

```html
<!DOCTYPE html>
<html>
<head><title>Home</title></head>
<body>
    <h1>Hello, Django!</h1>
</body>
</html>
```

## 🧩 MVT Architecture

| Component | Description |
|----------|-------------|
| **Model** | Handles database |
| **View** | Logic and data passing |
| **Template** | HTML presentation |

## 🗃 Models and Database

**models.py:**

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

Apply changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🛠 Admin Panel

1. Create superuser:

```bash
python manage.py createsuperuser
```

2. Register model in `admin.py`:

```python
from .models import Student
admin.site.register(Student)
```

3. Run server and go to `/admin/`

## 📥 Forms (Basic Example)

**forms.py:**

```python
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
```

## 📁 Static Files and Templates Setup

In `settings.py`:

```python
STATIC_URL = '/static/'

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
    },
]
```

Create folders:

```
project/
├── static/
├── templates/
```

## ✅ Useful Commands

| Command | Description |
|--------|-------------|
| `runserver` | Starts development server |
| `makemigrations` | Prepares model changes |
| `migrate` | Applies changes to database |
| `createsuperuser` | Creates admin login |
| `startapp` | Creates new app |

---
