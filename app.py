from flask import Flask, render_template, request, redirect, url_for, flash
from ai_model.predictor import predict
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        role = request.form.get("role")
        if not username:
            flash("Please enter a username", "warning")
            return render_template("core/login.html")
        if role == "teacher":
            return redirect(url_for("teacher_dashboard", teacher=username))
        return redirect(url_for("student_dashboard", student=username))
    return render_template("core/login.html")

@app.route("/student/<student>")
def student_dashboard(student):
    demo_features = [0.0, 1.0, 0.0, 0.5]
    pred = predict(demo_features)
    return render_template("student/dashboard.html", student=student, pred=pred)

@app.route("/teacher/<teacher>")
def teacher_dashboard(teacher):
    courses = [
        {"id": 1, "name": "Math 101", "students": 24},
        {"id": 2, "name": "Science 201", "students": 18},
    ]
    return render_template("teacher/dashboard.html", teacher=teacher, courses=courses)

@app.route("/teacher/<int:course_id>/view")
def course_view(course_id):
    course = {"id": course_id, "name": f"Course {course_id}", "students": []}
    return render_template("teacher/course_view.html", course=course)

if __name__ == "__main__":
    app.run(debug=True)
