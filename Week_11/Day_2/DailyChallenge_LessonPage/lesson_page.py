from flask import Flask, render_template
import markdown
import markdown.extensions.fenced_code

app = Flask(__name__)


def return_template(file_name):
    with open(file_name) as file:
        md_template = markdown.markdown(file.read(), extensions=['fenced_code'])
        return md_template


@app.route('/')
def complete():
    with open('templates/whole.md', 'w') as file:
        in_chapter_temp = return_template('templates/in-this-chapter.md')
        lesson_temp = return_template('templates/lesson.md')
        whole = in_chapter_temp + '<br>'*2 + lesson_temp
        file.write(whole)
    return return_template('templates/whole.md')


@app.route('/lesson')
def lesson():
    return return_template('templates/lesson.md')


@app.route('/in-this-chapter')
def chapter():
    return return_template('templates/in-this-chapter.md')


if __name__ == '__main__':
    app.run(debug=True)
