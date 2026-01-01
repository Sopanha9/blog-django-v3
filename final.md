# Project Presentation & Structure Guide

This guide is designed to help you present the "Blog Django V3" project. It breaks down where everything is located and explains the technical parts in simple terms.

---

## 1. Project Structure (Where things are)

Your project follows a clean, modular structure where the "backend logic" and "frontend display" are separated into different apps.

### Root Directory
*   `manage.py`: The command center. You use this to run the server (`runserver`), make migrations, and create superusers.
*   `db.sqlite3`: The database file where all your posts, comments, and users are stored.
*   `media/`: Stores user-uploaded files like the featured images for blog posts.

### The `apps` Folder
This is where the actual code lives. It is split into two main parts:

#### 1. `apps/api` (The Data Layer)
This app handles the database, administration, and data definitions.
*   **`models.py`**: The blueprint of your database. It defines what a "Post" and "Comment" look like (title, content, author, etc.).
*   **`admin.py`**: Controls the Dashboard. This is where you customized the jazzmin theme and added the rich text editor (CKEditor).
*   **`serializers.py`**: (Bonus) Converts your database models into JSON data, useful if you ever want to build a mobile app or a separate React frontend later.
*   **`urls.py`**: Defines the API endpoints (e.g., `/api/posts/`).

#### 2. `apps/blog` (The View Layer)
This app handles what the regular user sees on the website.
*   **`views.py`**: The logic behind the pages. It fetches data from the database (using Models) and decides which template to show.
    *   *Example*: `PostListView` grabs all public posts and sends them to the homepage.
*   **`urls.py`**: The URL map. It tells Django "When a user goes to `/post/my-slug`, show them the Detail View."
*   **`templates/`**: The HTML files. These are the actual pages users see, styled with Tailwind CSS.

---

## 2. Key Concepts Explained (For Slides)

Use these simple explanations when showing your code or features.

### The Flow of Data
1.  **User** requests a page (e.g., clicks a blog post).
2.  **URL (`urls.py`)** directs the request to the right View.
3.  **View (`views.py`)** asks the **Model (`models.py`)** for data (e.g., "Get me post #1").
4.  **Template (HTML)** receives the data and renders the beautiful page with Glassmorphism design.

### Why separate `api` and `blog`?
*   **Organization**: Keeps the "business logic" (data) separate from the "presentation" (website).
*   **Scalability**: If you want to add a mobile app later, your `api` app is already ready to serve data, while `blog` continues to serve the website.

### The "Magic" Parts
*   **CKEditor**: We didn't just use a simple text box. We integrated a full Rich Text Editor so admins can write formatted articles.
*   **Slugs**: Instead of `blog/1`, we use `blog/my-cool-post`. This is better for Google (SEO) and easier for humans to read.

---

## 3. Quick Presentation Checklist

*   **Show the Admin Panel**: Log in and show how easy it is to write a post.
*   **Show the Search**: Go to the homepage and search for a word to demonstrate the dynamic search (Bonus Feature).
*   **Show the Code**: Open `apps/api/models.py` to show how you defined the `Post` model.
*   **Show the Frontend**: Highlight the dark/light mode and the responsive design.
