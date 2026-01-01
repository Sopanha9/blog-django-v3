# Presentation Slides Script: Django Blog Project

**Structure Strategy**: We explain "Back to Front" (Foundation -> Database -> UI) as this follows the actual flow of data creation to presentation.

---

## Slide 1: Introduction & Team Roles
**Title**: Django Blog V3 - Group Assignment
**Subtitle**: A Full-Stack Monolithic Architecture

**Speaker Notes**:
"Welcome. We built a scalable blog application using Django. Here is how our team collaborated, broken down by our development layers:"

**Visual**: 
- **Reaksa**: Project Foundation (Configuration, Routing, Base Layouts)
- **Phanha**: Backend API (Database Models, Business Logic)
- **Sombath & Sophou**: Frontend (User Interface, Views, Templates)

---

## Slide 2: Project Architecture
**Title**: The "Back-to-Front" Architecture
**Visual**: A diagram showing layers.
`Database -> Models (API) -> Views (Blog) -> Templates (HTML)`

**Speaker Notes**:
"Our project is structured into two main applications to keep concerns separate:
1. **`apps/api`**: Handles the raw data and logic.
2. **`apps/blog`**: Handles what the user sees.
Everything is glued together by the **`main`** configuration."

---

## Slide 3: The Foundation (Reaksa)
**Title**: `main/` - The Control Center

**Key Files Explained**:
- **`settings.py`**: Tells Django which apps to use (`apps.api`, `apps.blog`) and configures the database.
- **`urls.py`**: The traffic controller. It tells the browser where to go.
  - `/admin` -> Administration
  - `/` -> Blog Pages
- **`templates/base.html`**: The master layout. It includes the Navbar and Footer so we don't have to rewrite them on every page.

**Speaker Notes**:
"Before any code could be written, Reaksa set up the environment. This ensures that when Phanha makes a model or Sombath makes a page, the system knows how to load them."

---

## Slide 4: The Backend (Phanha)
**Title**: `apps/api/` - The Data Layer

**Key Files Explained**:
- **`models.py`**: The Blueprint.
  - `class Post`: Defines Title, Content, Author.
  - `class Comment`: Defines relationships (Foreign Key to Post).
- **`admin.py`**: The Management Interface. We customized this so content creators can easily write blogs.

**Speaker Notes**:
"Phanha's role was to define *what* we are building. By creating the Models, he created the database structure that holds all our information."

---

## Slide 5: The Frontend (Sombath & Sophou)
**Title**: `apps/blog/` - The User Interface

**Key Files Explained**:
- **`views.py`**: The Logic. 
  - `def blog_list`: Fetches all public posts from Phanha's `Post` model.
  - `def blog_detail`: Fetches a single post and its comments.
- **`templates/blog/`**: The Visuals.
  - `blog_list.html`: loops through posts to show cards.
  - `blog_detail.html`: displays the full article.

**Speaker Notes**:
"Sombath and Sophou took the data provided by the backend and displayed it beautifully. They used Reaksa's `base.html` and filled it with Phanha's data."

---

## Slide 6: Putting it Together (Demo)
**Title**: The User Journey
**Visual**: Arrow flow
1. User visits `www.blog.com` -> **Reaksa's `urls.py`** catches it.
2. URL calls **Sombath's `views.py`**.
3. View asks **Phanha's `models.py`** for data.
4. Data is returned to the **Template** and sent to the User.

**Speaker Notes**:
"This seamless integration allows our team to work in parallel. While backend optimized the database, frontend polished the design."
