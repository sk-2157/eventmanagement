<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python" />
  <img src="https://img.shields.io/badge/Django-4.0+-green.svg" alt="Django" />
  <img src="https://img.shields.io/badge/face__recognition-enabled-ff69b4" alt="Face Recognition" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" />
</p>

# Event Management System with Facial Recognition

A robust, scalable **Event Management System** built with [Django](https://www.djangoproject.com/) that leverages facial recognition for secure and seamless event check-ins. This web application supports multi-user registration, real-time event updates, and secure role-based access control, making it ideal for modern event management needs.

## 📝 Description

- Developed a scalable Django-based web app supporting multi-user registration and management across multiple events with real-time updates.
- Integrated face recognition using OpenCV and the face_recognition library to automate user verification during event check-in.
- Implemented secure role-based access control (RBAC) using Django Auth and middleware, ensuring secure and scalable event access management.
- **Tools Used:** Python, Django, SQL, HTML, CSS, JavaScript, OpenCV

## 🚀 Features

- User registration and authentication (login/signup)
- Create, update, and delete events
- **Face recognition-based attendee verification and check-in (OpenCV + face_recognition)**
- Real-time event updates and notifications
- Manage event attendees & registrations
- Event scheduling with calendar support
- Automated email notifications & reminders
- Dashboard with analytics & reporting
- Secure role-based access control (RBAC) for admins and users
- Responsive web interface (HTML, CSS, JS)

## 🛠️ Tech Stack

- **Backend Framework:** Django (Python)
- **Face Recognition:** [face_recognition](https://github.com/ageitgey/face_recognition), OpenCV
- **Database:** SQL (e.g., SQLite, PostgreSQL)
- **Frontend:** HTML, CSS, JavaScript
- **Other Tools:** Django Auth, Bootstrap (if used)

## 💡 Face Recognition Integration

This project uses the powerful `face_recognition` Python library and OpenCV for verifying event attendees. During registration or check-in, attendees' faces are scanned and matched for secure and contactless entry.

**How it works:**
- Attendees upload their photo during registration.
- At event check-in, a live photo is captured and compared using face recognition.
- Only verified attendees are allowed entry.

## 💻 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sk-2157/eventmanagement.git
   cd eventmanagement
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install system dependencies for face recognition** (if not already installed):

   - **Ubuntu:**
     ```bash
     sudo apt-get install build-essential cmake
     sudo apt-get install libopenblas-dev liblapack-dev
     sudo apt-get install libx11-dev libgtk-3-dev
     sudo apt-get install python3-dev
     sudo apt-get install libboost-all-dev
     sudo apt-get install dlib
     ```
   - **For Windows/Mac:**  
     Please refer to the [face_recognition installation guide](https://github.com/ageitgey/face_recognition#installation).

5. **Apply Django migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Visit [http://localhost:8000](http://localhost:8000) to view the app.

## 📂 Project Structure

```
eventmanagement/
├── eventmanagement/    # Django project configuration
├── events/             # Main Django app (models, views, templates)
├── static/             # Static files (CSS, JS, images)
├── templates/          # Shared HTML templates
├── face_recognition/   # Face recognition related code/assets (if applicable)
├── manage.py
├── requirements.txt
└── ...
```

## 🧑‍💻 Usage

- Register/login as a user or admin.
- Upload your face photo during registration.
- Create and manage events via the dashboard.
- Check in to events using the face recognition feature.
- Admins can view analytics and manage all events.

## 🤝 Contributing

We welcome contributions! Please fork the repo and submit a pull request for any improvements or bug fixes.


---

<div align="center">
  <img src="https://img.shields.io/github/stars/sk-2157/eventmanagement?style=social" alt="Stars"/>
  <img src="https://img.shields.io/github/forks/sk-2157/eventmanagement?style=social" alt="Forks"/>
  <br>
  <strong>Made with ❤️ using Django, Python, OpenCV, and face_recognition</strong>
</div>
