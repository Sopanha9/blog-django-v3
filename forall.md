# Project Presentation Guide: 4 Key Pillars

This guide breaks down the project into 4 main technical points. For each point, show the specific file and explain the code logic.

---

## 📝 Presentation Sequence (The Flow)

**Recommendation: Explain "Back-to-Front"**
For a coding presentation, it is simplest to go **Back-to-Front** (Database $\to$ Logic $\to$ User Interface).
*   **Why?** It follows the dependency chain. You cannot explain how a "Search Bar" works (Frontend) until you explain how the data is stored (Backend).
*   **The Story:** "First we built the structure (1), then the database (2), then the logic to find data (3), and finally the tools to manage it (4)."

**Suggested Order of Speaking:**
1.  **Start High-Level**: "How is the project organized?" (Point 1) -> *Shows architecture.*
2.  **The Foundation (Back)**: "How is the data stored?" (Point 2) -> *Shows models.*
3.  **The Logic (Middle)**: "How does the search work?" (Point 3) -> *Shows views.*
4.  **The Controls (Management)**: "How do admins control it?" (Point 4) -> *Shows admin panel.*

---

## 1. Modular Architecture (The "Skeleton")
**📂 Location:** `main/urls.py`

**💻 Code to Show:**
```python
# main/urls.py
urlpatterns = [
    # ...
    path("blog/", include("blog.urls")),      # Routes for the Website
    path('api/', include('apps.api.urls')),   # Routes for the Backend Data
]
```

**🗣️ Explanation Script:**
"Our project isn't just one big file. We used a **Modular Architecture**.
*   Look at lines 31 and 32: We strictly separate the `blog/` URLs from the `api/` URLs.
*   The **Website (`apps.blog`)** runs independently from the **Data API (`apps.api`)**.
*   **Why?** This prevents spaghetti code. If the website design crashes, the API remains alive for other apps. It adheres to the 'Separation of Concerns' principle."

---

## 2. Smart Database Models (The "Brain")
**📂 Location:** `apps/api/models.py`

**💻 Code to Show:**
```python
# apps/api/models.py
class Post(models.Model):
    # ...
    slug = models.SlugField(...)  # SEO-friendly URLs
    content = RichTextUploadingField(...)  # CKEditor Integration
    is_public = models.BooleanField(default=True, ...) # Switch to hide/show posts
```

**🗣️ Explanation Script:**
"Here is the blueprint for our database. We aren't just storing text; we built a smart content system.
*   **Line 9 (`slug`)**: We use 'slugs' (like `/my-cool-post`) instead of IDs (`/1`), which helps with Google SEO.
*   **Line 11 (`RichTextUploadingField`)**: We bridged **CKEditor** here. This allows the admin to formatting text and upload images directly, instead of writing raw HTML.
*   **Line 8 (`is_public`)**: This acts as a 'Gatekeeper'. We can write a draft and save it (`False`), and it won't appear on the site until we switch this to `True`."

---

## 3. Efficient Views (The Logic)
**📂 Location:** `apps/blog/views.py`

**💻 Code to Show:**
```python
# apps/blog/views.py
def blog_list(request):
    # ...
    # Only fetch posts specifically marked as public
    base_qs = Post.objects.filter(is_public=True)
    
    # Search Logic
    if q:
        base_qs = base_qs.filter(
            Q(title__icontains=q) | 
            Q(content__icontains=q)
        )
```

**🗣️ Explanation Script:**
"This View acts as the traffic controller. It doesn't just blindly grab data.
*   **Line 11**: It intentionally filters `filter(is_public=True)`. This ensures that draft posts defined in the Model **never** leak out to the public website.
*   **Line 14-19**: We implemented a dynamic search here using `Q` lookups. It checks the title, content, and tags simultaneously.
*   This logic is then passed to the HTML template to render the cards you see on the screen."

---

## 4. Professional Admin & API (The Controls)
**📂 Location:** `main/settings.py`

**💻 Code to Show:**
```python
# main/settings.py
JAZZMIN_SETTINGS = {
    "site_title": "Blog CMS Admin",
    "site_header": "Blog CMS",
    # ...
    "icons": {
        "api.Post": "fas fa-blog",
    }
}
```

**🗣️ Explanation Script:**
"We went beyond the default settings to create a professional product.
*   **Jazzmin Configuration**: We overrode the default Django interface. By collecting these settings here, we transformed the admin panel into a branded dashboard with custom icons (`fas fa-blog`) and a sleek theme.
*   **Scalability**: Because we configured our Models properly in Point 2, this Admin panel automatically inherits the CKEditor and search tools, making it ready for client delivery immediately."
