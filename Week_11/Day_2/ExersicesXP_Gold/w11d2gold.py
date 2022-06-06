from flask import Flask, render_template_string
from datetime import datetime
from random import randint


app = Flask(__name__)


@app.route('/<int:some_number>')
def exercises(some_number):
    current_time = datetime.now()
    date_str = current_time.strftime('%H:%M')
    rand_number = randint(1, 100)
    template_string = '''
    Exercise 1: Current time
    <br><br>
    Current time: {{date_str}}
    <hr><br>
    Exercise 2: Current hour
    <br><br>
    Greeting: "
        {% if 8 <= hour < 13 %}
            'Good morning'
        {% elif 13 <= hour < 17 %}
            'Good afternoon'
        {% elif 17 <= hour < 21 %}
            Good evening
        {% else %}
            'Good night'
        {% endif %}
        "
    <hr><br>
    Exercise 3: Random number
    <br><br>
    {% if user == rand_num%}
        Success!
    {% endif %}
    <hr><br>'''
    return render_template_string(template_string, date_str=date_str,
                                  hour=current_time.hour, user=some_number,
                                  rand_num=rand_number)


if __name__ == "__main__":
    app.run(debug=True)
