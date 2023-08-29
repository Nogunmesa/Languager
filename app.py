from flask import Flask, render_template, request


app = Flask(__name__)

# Yoruba phrases
lessons = [
    {"lesson_id": 1, "title": "body parts", "content":["ori", "oju", "eti", "enu", "imu", "irun", "oju", "okan", "owo", "ika", "ese", "atelese"]}
]

@app.route('/')
def hello():
    return render_template('index.html', lessons=lessons)

app.route("/lesson/<int:lesson_id>")
def lesson(lesson_id):
    selected_lesson = None
    for lesson in lessons:
        if lesson["lesson_id"] == lesson_id:
            selected_lesson = lesson
            break
    return render_template("lesson.html", lesson=selected_lesson)