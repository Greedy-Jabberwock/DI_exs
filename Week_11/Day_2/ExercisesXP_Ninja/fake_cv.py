from faker import Faker
from flask import Flask, render_template
from random import randint


app = Flask(__name__)


@app.route('/')
def index():
    fake = Faker()
    fake_name = fake.name_male()
    fake_job = fake.job()
    random_img_number = randint(1, 1084)
    return render_template('index.html', title='CV', cv_name=fake_name,
                           job=fake_job, img_url=random_img_number)


@app.route('/email')
def email():
    fake = Faker()
    fake_email = fake.ascii_email()
    return render_template('mail.html', title='E-mail', email_str=fake_email)


if __name__ == '__main__':
    app.run(debug=True)
    # fake = Faker()
    # Faker.seed(0)
    # fake_name = fake.name()
    # fake_job = fake.job()
    # fake_email = fake.ascii_email()
    # print(fake_job)
    # print(fake_name)
    # print(fake_email)