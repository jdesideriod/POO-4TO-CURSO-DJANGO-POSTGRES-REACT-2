# Proyecto Django + React + PostgreSQL

Sistema web con **Django** (backend) y **plantillas HTML** para autenticación y manejo de notas, con estructura preparada para **React** y **Django REST Framework**.

## Tecnologías
- Django (Backend)
- Django REST Framework (DRF)
- React (Frontend) *(pendiente de uso en el repo actual)*
- PostgreSQL (Base de datos) *(configurable)*
- MySQL client (dependency actual en `requirements.txt`)

## Estructura del proyecto
- `backend/config/`: configuración global de Django (settings, urls, etc.)
- `backend/accounts/`: autenticación (login, logout, register) y modelo de usuario
- `backend/core/`: funcionalidad principal (dashboard y notas)
- `backend/templates/`: plantillas base
- `backend/*/templates/`: plantillas por app (`accounts/`, `core/`)

## Requisitos
- Python 3.10+ (o compatible)
- Un motor de base de datos configurado mediante variables de entorno
- Paquetes listados en `backend/requirements.txt`

## Instalación

### Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Variables de entorno
El proyecto usa `python-decouple` (`backend/config/settings.py`). Se espera, como mínimo:

- `DJANGO_SECRET_KEY`: clave secreta de Django
- `DJANGO_DEBUG`: `true/false` (por defecto `false`)
- `DJANGO_ALLOWED_HOSTS`: lista separada por coma (por defecto `localhost,127.0.0.1`)

Configuración de base de datos (en `DATABASES`):
- `DB_ENGINE` (por defecto `django.db.backends.mysql`)
- `DB_NAME` (por defecto `ventas_db_local`)
- `DB_USER` (por defecto `root`)
- `DB_PASSWORD` (por defecto `Ja011017`)
- `DB_HOST` (por defecto `localhost`)
- `DB_PORT` (por defecto `3306`)

> Nota: aunque el README menciona PostgreSQL, en `settings.py` el `DB_ENGINE` por defecto está configurado para **MySQL**. Ajusta `DB_ENGINE` si deseas PostgreSQL.

## Uso (rutas)
Después de ejecutar `runserver`, accede a:

### Autenticación
- **Login**: `http://127.0.0.1:8000/auth/login/`
- **Registro**: `http://127.0.0.1:8000/auth/register/`
- **Logout**: `http://127.0.0.1:8000/auth/logout/`

### Notas
- **Dashboard** (lista de notas del usuario): `http://127.0.0.1:8000/dashboard/`
- **Crear nota**: `http://127.0.0.1:8000/dashboard/nueva/`
- **Eliminar nota**: `http://127.0.0.1:8000/dashboard/eliminar/<pk>/`

## Flujo básico (login/notas)
1. El usuario crea una cuenta en `POST /auth/register/` (vía vista `RegisterView`) o entra con su cuenta.
2. Inicia sesión en `GET /auth/login/`.
3. El sistema redirige a `GET /dashboard/`.
4. Desde el dashboard puede:
   - crear una nota (`/dashboard/nueva/`)
   - eliminar una nota (`/dashboard/eliminar/<pk>/`)

## Notas
- Las notas pertenecen al usuario autenticado (se filtran por `owner=self.request.user`).
- Las vistas principales usan mixins de Django (`LoginRequiredMixin`) para evitar accesos no autenticados.

