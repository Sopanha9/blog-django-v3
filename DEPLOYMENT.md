# Deployment Guide

This project is configured for deployment on platforms like [Render](https://render.com), [Railway](https://railway.app), or [Heroku](https://heroku.com).

## Prerequisites

- [Git](https://git-scm.com/) installed
- Accounts on the hosting platform of your choice (e.g., Render)

## Deploying to Render (Recommended)

Render is a popular choice for Django apps as it offers a free tier for web services and PostgreSQL databases.

### 1. Push to GitHub

Ensure your code is pushed to a GitHub repository:

```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### 2. Create a Database on Render

1. Log in to your Render dashboard.
2. Click **New +** and select **PostgreSQL**.
3. Give it a name (e.g., `blog-db`).
4. Select the **Free** plan.
5. Click **Create Database**.
6. Keep this tab open; you'll need the **Internal Database URL** shortly.

### 3. Create a Web Service

1. Go back to Dashboard, Click **New +** and select **Web Service**.
2. Connect your GitHub repository.
3. Configure the following:
   - **Name**: `blog-cms` (or your choice)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn main.wsgi`
4. **Environment Variables**:
   Add the following environment variables:
   - `PYTHON_VERSION`: `3.11.5` (or your local version)
   - `SECRET_KEY`: (Generate a long random string)
   - `DEBUG`: `False`
   - `DATABASE_URL`: (Paste the **Internal Database URL** from the database you created in Step 2)
   - `ALLOWED_HOSTS`: `*` (or your specific render domain, e.g. `blog-cms.onrender.com`)

5. Click **Create Web Service**.

### 4. Create Superuser (Optional)

Once deployed, you can create a superuser by accessing the Render Shell (in the dashboard for your Web Service) and running:
```bash
python manage.py createsuperuser
```

## Configuring other platforms

### Heroku / Railway

The `Procfile` is already included:
```
web: gunicorn main.wsgi
```

Ensure you set the same Environment Variables (`SECRET_KEY`, `DEBUG`, `DATABASE_URL`, `ALLOWED_HOSTS`) in their respective dashboards.

## Important Notes

- **Static Files**: `Whitenoise` is configured to serve static files.
- **Media Files**: Useruploaded images (`media/`) are **NOT** persistent on Render/Heroku's free tier (ephemeral filesystem). 
  - For production, if you need persistent image uploads, you should configure AWS S3 or similar storage. (This requires additional setup: `django-storages`).
