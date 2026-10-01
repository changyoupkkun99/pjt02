# AGENTS.md

This repository is a small Django project with custom authentication and a todo API. Keep changes aligned with the existing Django + DRF structure and avoid broad refactors unless the task specifically requires them.

## Project layout

- Django project root: [crud/settings.py](crud/settings.py), [crud/urls.py](crud/urls.py)
- Custom user model: [accounts/models.py](accounts/models.py)
- Todo model: [todos/models.py](todos/models.py)
- Auth/registration helpers: [accounts/serializers.py](accounts/serializers.py)
- App URL config: [todos/urls.py](todos/urls.py)

## Working conventions

- Prefer app-local changes: keep models, serializers, views, and URL patterns in the relevant app directory.
- This project uses a custom user model: `accounts.User`. Do not replace it with Django's default auth user unless the task explicitly requires it.
- The project already includes `dj-rest-auth`, `django-allauth`, and `djangorestframework`. Keep auth-related customizations compatible with those packages.
- The root URL config mounts the todo API under `api/v1/` and auth routes under `/accounts/`.
- SQLite is the active database backend; keep the default configuration unless the task explicitly changes it.
- When adding or changing models, include the matching migration and keep migrations in the app's `migrations/` folder.
- Prefer small, targeted edits over large rewrites. Most additions here should stay backend-focused.

## Common commands

Run these from the project root:

- Activate the local venv: `source .venv/Scripts/activate` (Git Bash / WSL) or `.venv\Scripts\activate` (PowerShell/CMD)
- Start the app: `python manage.py runserver`
- Apply schema changes: `python manage.py makemigrations && python manage.py migrate`
- Run tests: `python manage.py test`
- Open Django shell: `python manage.py shell`

## AI guidance

- Respect the existing app boundaries and naming conventions.
- Avoid unnecessary changes to settings, routes, or authentication behavior unless the request calls for them.
- When implementing endpoints, prefer Django REST Framework patterns already used by the rest of the project.
- Keep the code readable and explicit; this project is intentionally small and easy to follow.
- If a change touches auth or database schema, verify the effect with the relevant Django management command before concluding the work.
