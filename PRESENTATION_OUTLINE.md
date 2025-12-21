# Project Presentation: Blog CMS with Admin Extensions

## 1. Project Overview

**Objective:** Build a professional, full-featured Content Management System (CMS) for blogging with a focus on SEO, user engagement, and a highly customized administrative experience.

---

## 2. Core Features (Teacher Requirements)

### ✅ Data Modeling

- **Post Model**: Stores blog content, metadata, and SEO slugs.
- **Comment Model**: Enables reader interaction with approval workflows.
- **Category & Tags**: Implemented as flexible fields for content organization.

### ✅ SEO & Content Creation

- **Slug Auto-generation**: Slugs are automatically created from titles in the admin panel for SEO-friendly URLs (e.g., `/blog/my-first-post/`).
- **CKEditor Integration**: A powerful Rich Text Editor (RTE) for writing content with support for images, formatting, and media uploads.

### ✅ User Experience (Frontend)

- **List View**: A clean, 3-column grid layout showing all public posts.
- **Detail View**: Full post reading experience with a dedicated comment section.
- **Comment System**: Readers can submit comments which are displayed instantly under posts.

### ✅ Advanced Admin Customization

- **Jazzmin Theme**: Modernized the default Django admin with a professional dashboard.
- **Custom UI**: Injected custom CSS to fix layout issues and expand the CKEditor workspace.
- **Admin Tools**:
  - Searchable posts and comments.
  - Filters by category, author, and date.
  - Direct editing of "Public" status from the list view.

---

## 3. Bonus Features Implemented

### 🚀 Pagination

- Implemented Django's `Paginator` to handle large volumes of posts.
- Clean navigation buttons with support for maintaining search queries across pages.

### 🚀 Post Search

- Integrated a global search bar on the blog list page.
- Users can search by **Title, Content, Category, Tags, or Author**.

### 🚀 Featured Media

- Support for **Featured Images** on every post to improve visual appeal.

### 🚀 Modern UI/UX

- **Dark/Light Mode**: Fully responsive theme toggle for better readability.
- **Glassmorphism Design**: Modern UI using Tailwind CSS and backdrop blurs.

---

## 4. Technical Stack

- **Backend**: Django 5.2
- **Database**: SQLite3
- **Frontend**: Tailwind CSS, JavaScript (Theme Toggle)
- **Editor**: django-ckeditor
- **Admin UI**: django-jazzmin + Custom CSS

---

## 5. User Stories (Validation)

1. **Reader**: "I can browse the blog list, search for specific topics, and read detailed articles."
2. **Admin**: "I can easily manage content through a beautiful dashboard, with a large editor for writing."
3. **User**: "I can leave feedback on posts through the comment section."

---

## 6. Team Review Notes

- **Code Structure**: Apps are separated into `api` (models/admin) and `blog` (frontend views).
- **SEO**: All URLs use slugs instead of IDs.
- **Performance**: Images are handled via `Pillow` and served through media roots.
