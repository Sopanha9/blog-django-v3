# 4 Main Points for Code Presentation

This guide breaks down the project into 4 key technical pillars, ideal for explaining the codebase to a teacher or evaluator.

---

## 1. Project Architecture (The "Skeleton")
**Goal:** Explain how the files are organized and why.

*   **Modular Design**: Instead of a monolithic structure, we split the project into two distinct apps:
    *   `apps/api`: Handles "business logic" and data (Database models, Administration tools).
    *   `apps/blog`: Handles "user interface" (What the user sees, HTML templates, website navigation).
*   **Why it's good**: This follows the **Separation of Concerns** principle. It decouples the data management (Back office) from the presentation layer (Website), making the code cleaner, easier to debug, and more scalable.

## 2. Backend Models & Database (The "Brain")
**Goal:** Explain how data is stored and structured.
*   **File to Reference**: `apps/api/models.py`
*   **Key Components**:
    *   **Post Model**: The core entity. It stores more than just text; it handles `slugs` (for SEO-friendly URLs), `featured_image` uploads, and integrates **CKEditor** for rich text data.
    *   **Comment Model**: Handles user interaction via a `ForeignKey` relationship to Posts.
    *   **Data Integrity**: We utilize boolean fields like `is_public` and `is_approved` as "gatekeepers," ensuring only valid, moderated content reaches the public facing site.

## 3. Frontend Views & Templates (The "Face")
**Goal:** Explain how the user interfaces with the data.
*   **Files to Reference**: `apps/blog/views.py` and `apps/blog/templates/`
*   **Pattern**: We utilize the **MVT (Model-View-Template)** architecture.
    *   **View Layer**: Fetches specific datasets (e.g., "Latest 5 posts") using efficient database queries.
    *   **Template Layer**: Renders that data dynamically into HTML.
*   **Design Implementation**: The frontend isn't just basic HTML; it implements a custom **Glassmorphism** design system with responsive layouts that adapt to mobile and desktop screens.

## 4. Admin Panel & Extensibility (The "Controls")
**Goal:** Explain management features and future-proofing.
*   **File to Reference**: `main/settings.py` (specifically `JAZZMIN_SETTINGS`)
*   **Professional Admin**: We replaced the default Django admin with **Jazzmin**. This provides a branded, user-friendly dashboard for content managers to write posts and moderate comments easily.
*   **API Readiness**: We built a `REST_FRAMEWORK` layer (in `apps/api/serializers.py`). This exposes our data as JSON, meaning the backend is "Headless-ready" — capable of powering a future Mobile App (iOS/Android) without changing the core logic.
