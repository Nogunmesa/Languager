from flask import Flask, render_template, request

app = Flask(__name__)

# Sample Yoruba vocabulary and phrases
lessons = [
    {"lesson_id": 1, "title": "Colors", "content": ["ọrun", "pupa", "dúdú"]},
    {"lesson_id": 2, "title": "Animals", "content": ["ẹja", "ẹlẹ́phantí", "àkọ́kọ́"]},
    # Add more lessons
]

@app.route("/")
def index():
    return render_template("index.html", lessons=lessons)

@app.route("/lesson/<int:lesson_id>")
def lesson(lesson_id):
    selected_lesson = None
    for lesson in lessons:
        if lesson["lesson_id"] == lesson_id:
            selected_lesson = lesson
            break
    return render_template("lesson.html", lesson=selected_lesson)

if __name__ == "__main__":
    app.run(debug=True)
