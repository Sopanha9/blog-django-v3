# Blog CMS Admin System

A full-featured Django-based Content Management System for managing blog posts with a REST API, rich text editing, and comment functionality.

## Features

- 📝 Rich text editor (CKEditor) for blog content
- 🖼️ Image upload support for featured images
- 🏷️ Categories and tags for post organization
- 💬 Comment system with moderation
- 🔒 Admin interface for content management
- 🚀 RESTful API for programmatic access
- 📱 Responsive design templates

## Tech Stack

- **Framework**: Django 5.2.8
- **Database**: SQLite
- **REST API**: Django REST Framework
- **Rich Text Editor**: CKEditor
- **Frontend**: HTML templates with custom CSS
- **Python**: 3.x

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd blog_cms
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin
   - API endpoints: http://localhost:8000/api

## Project Structure

```
blog_cms/
├── apps/
│   ├── api/          # REST API endpoints and serializers
│   └── blog/         # Blog app with views and templates
├── main/             # Project settings and configuration
├── media/            # User-uploaded files
├── resources/        # Static resources (CSS, images)
├── db.sqlite3        # SQLite database
├── manage.py         # Django management script
└── requirements.txt  # Python dependencies
```

## Usage

### Admin Panel

1. Navigate to http://localhost:8000/admin
2. Log in with your superuser credentials
3. Create, edit, or delete blog posts
4. Manage comments and user submissions
5. Configure post visibility and metadata

### Creating a Blog Post

1. Go to Admin Panel → Blog Posts → Add Blog Post
2. Fill in the required fields:
   - **Title**: Post title
   - **Author**: Author name
   - **Content**: Rich text content using the editor
   - **Slug**: Auto-generated URL-friendly identifier
   - **Category**: Post category
   - **Tags**: Comma-separated tags
   - **Featured Image**: Optional header image
   - **Is Public**: Toggle to publish/unpublish
3. Click "Save"

### API Endpoints

- `GET /api/posts/` - List all published posts
- `GET /api/posts/<id>/` - Get a specific post
- `POST /api/posts/` - Create a new post (requires authentication)
- `PUT /api/posts/<id>/` - Update a post (requires authentication)
- `DELETE /api/posts/<id>/` - Delete a post (requires authentication)

## Models

### Post
- `title` - Blog post title
- `author` - Author name
- `content` - Rich text content
- `slug` - URL-friendly identifier
- `category` - Post category
- `tags` - Comma-separated tags
- `featured_image` - Optional image
- `is_public` - Publication status
- `date_created` - Creation timestamp
- `date_updated` - Last update timestamp

### Comment
- `post` - Related blog post
- `name` - Commenter name
- `email` - Commenter email
- `content` - Comment text
- `is_approved` - Moderation status
- `date_created` - Creation timestamp

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

## Configuration

Key settings are located in `main/settings.py`:

- `DEBUG`: Set to `False` in production
- `SECRET_KEY`: Change this for production deployment
- `ALLOWED_HOSTS`: Add your domain names
- `DATABASES`: Configure your production database

## Security Notes

⚠️ **Important for Production:**

1. Set `DEBUG = False`
2. Generate a new `SECRET_KEY`
3. Update `ALLOWED_HOSTS` with your domain
4. Use a production database (PostgreSQL recommended)
5. Configure proper media file storage
6. Set up HTTPS
7. Enable CSRF protection

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please open an issue in the repository.


