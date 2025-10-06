# Task Manager App

A web-based task management application built with **Django** that allows users to **register, log in, and manage their personal tasks securely**. Users can add, edit, and delete tasks, and view tasks specific to their account, making it a personalized and secure task tracking solution.

---

## Features

- **User Authentication**
  - Secure registration, login, and logout system.
- **Task Management**
  - Create, edit, and delete tasks.
  - View tasks specific to the logged-in user.
- **Deadline Tracking**
  - Set deadlines for each task.
- **User-friendly Interface**
  - Simple and intuitive navigation.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jmdaragosa/task-manager-app.git
   cd task-manager-app

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    
3. **Activate the virtual environment, install dependencies, apply migrations, create superuser, run server, and access the app:**

- **Activate the virtual environment:**  
  - On Windows:
    ```bash
    venv\Scripts\activate
    ```  
  - On Mac/Linux:
    ```bash
    source venv/bin/activate
    ```

- **Install dependencies:**
  ```bash
  pip install -r requirements.txt

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser

6. Run the development server:
   ```bash
   python manage.py runserver

7. Access the app
   Open your browser and go to http://127.0.0.1:8000/

# Usage
1. Register a new account via /register/.
2. Login via /accounts/login/.
3. Create, view, edit, and delete tasks from the dashboard.
4. Logout via /accounts/logout/.

# Future Enhancements

1. Add task categories or priorities.
2. Add search and filtering for tasks.
3. Responsive UI for mobile devices.
4. Deploy to a live server (e.g., Heroku, Render).
