from flask import Flask, render_template

app = Flask(__name__)

# Sample data
lessons = [
    {"lesson_id": 1, "title": "Body Parts", "content": ["ori", "oju", "imu", "enu", "eti", "irun", "owo", "ese", "okan", "ika", "atelese"]}
]

@app.route('/')
def index():
    return render_template('index.html', lessons=lessons)

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    lesson = next((l for l in lessons if l["lesson_id"] == lesson_id), None)
    if lesson is None:
        return "Lesson not found", 404
    return render_template('lesson.html', lesson=lesson)

if __name__ == "__main__":
    app.run(debug=True)
