 
# 📝 Flask Blog Web App

A full-featured blog web application built with Flask, focusing on authentication, user management, and secure backend practices.

---

## 🚀 Overview

This project is a multi-user blog platform where users can register, log in, create posts, and interact through comments.
It demonstrates core backend concepts such as authentication, authorization, and database relationships.

---

## 🔥 Features

### 👤 Authentication System

* User registration
* Login / Logout
* Password reset functionality
* Secure password hashing

---

### 📝 Blog System

* Create, edit, and delete posts (CRUD)
* View all posts on main page
* Individual post page with full content

---

### 💬 Comments System

* Add comments on posts
* Each comment linked to its author and post

---

### 📊 User Dashboard

* View personal information
* See user's posts
* See user's comments

---

### 🔐 Security Features

* Password hashing (no plain text storage)
* Authorization checks (users can only modify their own content)
* Protected routes using login system

---

## 🧠 Tech Stack

* **Backend:** Flask
* **Database:** SQLite + SQLAlchemy
* **Authentication:** Flask-Login
* **Frontend:** HTML, CSS, Bootstrap

---
## Screen Shots
### Home Page
![Home Page](./screenshots/home_page.png)
<hr>

### User Dashboard
![User Dashboard](./screenshots/profile_page.png)

### Editing User details
![Editing User Page](./screenshots/edit_user.png)


### Post Detail View
![Post Detail](./screenshots/post_in_details.png)
Individual post page with full content, comments section, and options to edit or delete (if authorized).

### Create/Edit Post
![Create Post](./screenshots/create_post.png)
Form interface for creating new blog posts or editing existing ones with title, content, and submission options.

### User Authentication
![Login Page](./screenshots/signup_page.png)
<hr>

![Login Page](./screenshots/login_page.png)
Secure login interface with credentials validation and link to registration for new users.
<hr>

![Reset Password Page](./screenshots/reset_password.png)



---

## 🗂️ Project Structure

```
.
└── flask_blog
    ├── app
    │   ├── auth
    │   │   ├── forms.py
    │   │   ├── __init__.py
    │   │   └── views.py
    │   ├── extensions.py
    │   ├── __init__.py
    │   ├── main
    │   │   ├── forms.py
    │   │   ├── __init__.py
    │   │   └── views.py
    │   ├── models.py
    │   ├── services
    │   │   ├── forms.py
    │   │   ├── __init__.py
    │   │   └── views.py
    │   ├── static
    │   │   ├── css
    │   │   │   └── style.css
    │   │   └── pics
    │   │       ├── default.jpg
    │   │       └── default_post.jpg
    │   ├── templates
    │   │   ├── auth
    │   │   │   ├── change_password.html
    │   │   │   ├── login.html
    │   │   │   └── signup.html
    │   │   ├── base.html
    │   │   ├── main
    │   │   │   ├── dashboard.html
    │   │   │   ├── home.html
    │   │   │   ├── post_detail.html
    │   │   │   └── posts.html
    │   │   └── services
    │   │       ├── create_post.html
    │   │       ├── edit_post.html
    │   │       └── edit_profile.html
    │   └── utilities.py
    ├── config.py
    ├── README.md
    └── run.py


```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/flask-blog.git
cd flask-blog
```

2. Create virtual environment:

```
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
python run.py
```

---

## 🎯 Learning Goals

This project was built to:

* Understand Flask backend development
* Learn authentication and session handling
* Practice secure coding concepts
* Prepare for web security and penetration testing

---

## ⚠️ Notes

This is a learning project and may not include full production-level security.

---

## 👨‍💻 Author

mostafa-12 (Mostafa Ahmed Gaber)
