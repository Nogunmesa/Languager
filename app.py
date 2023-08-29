from flask import Flask, render_template

app = Flask(__name__)

# Sample data
class Lesson:
    def __init__(self, lesson_id, title, content):
        self.lesson_id = lesson_id
        self.title = title
        self.content = content

lessons = [
    Lesson(1, "Lesson 1", ["Content 1", "Content 2"]),
    Lesson(2, "Lesson 2", ["Content 3", "Content 4"]),
    # Add more lessons as needed
]

@app.route('/')
def index():
    return render_template('index.html', lessons=lessons)

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    lesson = next((l for l in lessons if l.lesson_id == lesson_id), None)
    if lesson is None:
        return "Lesson not found", 404
    return render_template('lesson.html', lesson=lesson)

if __name__ == "__main__":
    app.run(debug=True)
