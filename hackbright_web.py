"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""


    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grades = hackbright.get_grades_by_github(github)

    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades=grades)


@app.route("/")
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    """Add a student"""

    return render_template("student_add.html")


@app.route("/success", methods=["POST"])
def add_student():
    """added a student"""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')
    hackbright.make_new_student(first, last, github)

    return render_template("success.html",
                            first=first,
                            last=last,
                            github=github)

@app.route("/pick-project")
def choose_project():
    """Chooses a project"""

    return render_template("pick_project.html")


@app.route("/project")
def display_project():
    """Displays projects"""

    title = request.args.get('project')
    row = hackbright.get_project_by_title(title)
    rows = hackbright.get_grades_by_title(title)
    description = row[1]
    max_grade = row[2]

    return render_template("display_project.html",
                            title=title,
                            description=description,
                            max_grade=max_grade,
                            rows=rows)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
