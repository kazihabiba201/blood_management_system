# Blood Management System

A **Django-based Blood Management System** designed to manage blood banks, donors, and blood donation requests. The system provides separate dashboards for **admins** and **donors**, allowing efficient management and tracking of blood donations.

---

## Features

### Admin
- Add, update, and view blood bank details.
- Approve or reject blood donation requests.
- View total donors and pending requests.
- Dashboard statistics for blood banks and donation units.

### Donor
- Register and log in as a donor.
- Submit blood donation requests.
- View donation history and status of requests.

---

## Technologies Used

- **Backend:** Python 3.x, Django 5.x  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **Database:** MySQL  
- **API:** Django Rest Framework (optional for API endpoints)  
- **Deployment:** Vercel (or any WSGI-compatible hosting)  
- **Other:** Django Crispy Forms for better form rendering  

---

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/kazihabiba201/blood_management_system
cd blood_management_system
```
2. Create and Activate Virtual Environment
```bash

python -m venv venv
```
Windows:

```bash

venv\Scripts\activate
```
3. Install Dependencies
```bash

pip install -r requirements.txt
```
4. Configure Database
Edit blood_management_system/settings.py to set your MySQL database credentials:

python
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blood_management_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
5. Apply Migrations
```bash

python manage.py makemigrations
python manage.py migrate
```
6. Create Superuser (Admin)
Create an admin user to access Django’s admin panel:

```bash

python manage.py createsuperuser
```
Enter a username, email, and password when prompted.

This superuser can log in to the admin panel at /admin/.

7. Collect Static Files
```bash
python manage.py collectstatic
```
Running the Application Locally
```bash

python manage.py runserver
Open http://127.0.0.1:8000 to access the login page.
```
Deployment on Vercel
1. Install Vercel CLI
```bash

npm i -g vercel
```
2. Log in to Vercel
```bash

vercel login
```
3. Prepare Deployment Files
Ensure these files exist in your project root:

requirements.txt

Procfile (example: web: gunicorn blood_management_system.wsgi)


4. Deploy the Project
bash
Copy code
vercel
Your login page will be the first page after deployment.

URL Routes
```
/login/ – Donor or Admin login page

/register/ – Registration page

/dashboard/ – Donor dashboard

/admin-dashboard/ – Admin dashboard

/logout/ – Logout

/approve-request/<id>/ – Admin approves a donation request

/reject-request/<id>/ – Admin rejects a donation request
```
Default Roles
Admin: can manage blood banks, approve/reject requests, and view dashboard stats
Donor: can submit donation requests and view personal history

## Screenshots

| Login Screen | Register Screen |
|--------------|----------------|
| ![Login](https://github.com/user-attachments/assets/1521e120-848c-4b44-a979-89fb037a9eb0) | ![Register](https://github.com/user-attachments/assets/7866af58-6f19-4b3c-9671-301128642dd2) |

| Donor Dashboard | Admin Dashboard |
|-----------------|----------------|
| ![Donor Dashboard](https://github.com/user-attachments/assets/24e940d5-dfaf-4c38-8372-fe18092cd882) | ![Admin Dashboard](https://github.com/user-attachments/assets/f0e90da4-ac72-4e6c-b297-1699c166b3ca) |



