# Sustagram 🌿

Sustagram is a Django-powered social media platform designed to promote sustainability and environmental awareness. Users can share eco-friendly actions, track their green scores, follow others, and engage with a like-minded community. Built with Tailwind CSS and Chart.js for a modern, responsive interface.

---

## 🚀 Features

### Core Functionality
- User authentication: signup, login, logout
- Custom User model with roles: Individual, NGO, Company
- Profile pages with green score, badges, bio
- Upload posts with captions, tags, and images
- General and personal feeds (explore + following)
- Comments on posts, with delete functionality
- Follow/unfollow users
- Leaderboard of top contributors
- Dashboard with:
  - Green score overview
  - Weekly activity chart (Chart.js)
  - Badge progress tracker
- Weekly green score reset for inactive users

### Frontend
- Tailwind CSS for responsive UI
- Mobile-friendly layout
- Fully themed UI with dark green and neutral palette
- Mobile navbar with toggle menu

---

## 🛌 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/sustagram.git
cd sustagram
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Tailwind
Follow the guide here: https://django-tailwind.readthedocs.io/en/latest/installation.html
```bash
python manage.py tailwind install
yarn build  # or npm run build inside theme/static_src
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create superuser
```bash
python manage.py createsuperuser
```

### 7. Enable Live Reload (optional but recommended)
Install Django Browser Reload: https://pypi.org/project/django-browser-reload/
```bash
pip install django-browser-reload
```
Add to `INSTALLED_APPS` and include `{% browser_reload_script %}` in your base template.

### 8. Run development server
Open **two terminals**:

Terminal 1 – Django server:
```bash
python manage.py runserver
```

Terminal 2 – Tailwind watcher:
```bash
python manage.py tailwind start
```

Visit http://127.0.0.1:8000/ to start using Sustagram locally.

---

## 📄 Project Structure
```
sustagram/
├── users/             # Custom User model, auth, profile, follow
├── posts/             # Posts, tags, comments
├── theme/             # Tailwind CSS integration
├── templates/         # Global template directory
├── static/            # Compiled Tailwind assets
├── media/             # Uploaded images
├── manage.py
├── requirements.txt
```

---

## 💡 Developer Notes
- Whenever a new model is created, register it with Django admin
- All templates are centralized in the root `templates/` folder
- Views are modularized under each app using `views/` package
- Green score is reset weekly via a management command
- Use Chart.js for dashboard charts
- Mobile nav toggle relies on `classList.toggle('hidden')`
- Meta viewport tag must be present for responsiveness

---

## ✨ Future Improvements
- Weekly green goal tracking
- Score history chart
- Notifications (comments, follows)
- Avatar upload
- Explore page with trending tags
- Settings page (email/password)

---