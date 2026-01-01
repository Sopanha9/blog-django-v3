# Project Structure

## Root Directory
- **main/**: Core project configuration (settings, URLs, WSGI/ASGI).
- **apps/**: modular Django apps.
- **manage.py**: Django's command-line utility.
- **db.sqlite3**: SQLite database file.
- **media/**: User-uploaded content (images, etc).

## Apps
### apps/api (Backend)
Handles data structure and API endpoints. 
- `models.py`: Database definitions (Post, Comment).
- `serializers.py`: Data conversion for APIs.
- `views.py`: API logic (ViewSets).

### apps/blog (Frontend)
Handles user-facing pages.
- `views.py`: Renders HTML pages.
- `templates/`: HTML files for the blog.

## Configuration
### main/
- `settings.py`: Global settings (apps, middleware, database, templates).
- `urls.py`: Main URL routing.
- `templates/`: Base templates (e.g., specific base layouts).
