# AI-Powered Student Management System 🎓

This is a Project-Based Learning (PBL) project that implements a Student Management System using Django. The system includes role-based access for Admins, Teachers, and Students, and features an AI model to detect and flag "at-risk" students.

## 🚀 Key Features

### Admin
* **Full System Control:** Admins use the built-in Django Admin Panel (`/admin`).
* **User Management:** Create, Read, Update, and Delete Student and Teacher accounts.
* **Course Management:** Create courses, assign teachers to courses, and enroll students in courses.
* **Data Management:** Manage all grades and attendance records.

### Teacher
* **Teacher Dashboard:** View a list of all assigned courses.
* **Course View:** See a complete roster of students for each course.
* **Gradebook:** Enter and update grades for students' assignments and quizzes.
* **Attendance Module:** Mark student attendance (Present/Absent) for each class.
* **🤖 AI Feature: At-Risk Detector:** Automatically see a visual "At-Risk" flag next to any student who is predicted to be in danger of failing, allowing for early intervention.

### Student
* **Student Dashboard:** View all enrolled courses in one place.
* **Progress Tracking:** See current grades and attendance percentage for each course.
* **Report Generation:** Download a simple PDF report of semester grades.

## 🛠️ Tech Stack

* **Backend:** **Python** with the **Django** framework
* **Frontend:** **Django Templates** (HTML, CSS, JavaScript)
* **Database:** **SQLite** (default for development)
* **UI/Styling:** **Bootstrap 5**
* **AI/ML:** **Scikit-learn** and **Pandas** for the prediction model

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
cd pbl_project_root
