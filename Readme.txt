Little Lemon Restaurant API - Coursera Backend Capstone
======================================================

Project features
- Django serves a static HTML home page.
- Django REST Framework menu and booking APIs.
- MySQL database configuration (default).
- User registration and token authentication.
- Unit tests.
- Django admin interface.

API paths to test
-----------------
GET/POST/PUT/PATCH/DELETE /api/menu/
GET/PUT/PATCH/DELETE     /api/menu/<id>/
POST                     /api/registration/
POST                     /api/api-token-auth/
GET/POST                 /api/bookings/
GET/PUT/PATCH/DELETE     /api/bookings/<id>/

Authentication
--------------
Use POST /api/registration/ with JSON:
{"username":"demo","email":"demo@example.com","password":"StrongPass123!"}

The response contains a token. In Insomnia, add header:
Authorization: Token YOUR_TOKEN

Booking endpoints require authentication. Menu reads are public; menu changes require a staff account.

Setup (Windows / VS Code)
-------------------------
1. Install Python 3.10+ and MySQL Server.
2. In MySQL, create the database:
   CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
3. Open this folder in VS Code and create a virtual environment:
   py -m venv .venv
   .venv\\Scripts\\activate
4. Install packages:
   python -m pip install --upgrade pip
   pip install -r requirements.txt
5. Copy .env.example to .env and update the MySQL credentials.
   Note: This starter settings file reads environment variables directly; set them
   in the VS Code terminal before running Django, or add python-dotenv and load .env.
   Example PowerShell commands:
   $env:DB_NAME="littlelemon"
   $env:DB_USER="root"
   $env:DB_PASSWORD="your_mysql_password"
   $env:DB_HOST="127.0.0.1"
   $env:DB_PORT="3306"
6. Run:
   python manage.py makemigrations restaurant
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
7. Visit http://127.0.0.1:8000/ and http://127.0.0.1:8000/api/menu/

Run unit tests
--------------
python manage.py test

Quick test without MySQL
------------------------
For a temporary local smoke test only, set:
$env:DB_ENGINE="sqlite"
Then run migrations and tests. Switch back to MySQL before claiming the MySQL
integration requirement is verified.

GitHub submission
-----------------
Create a new empty GitHub repository, then run in this project folder:
git init
git add .
git commit -m "Complete Little Lemon API capstone"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/little-lemon-api.git
git push -u origin main

Replace YOUR_USERNAME and use your actual repository URL. Do not upload database
passwords or secret keys. Confirm the README and code are visible on GitHub.
