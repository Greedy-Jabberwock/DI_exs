import os


class Config:
    db_info = {
        'host': 'localhost',
        'database': 'cryptos',
        'psw': 'learningSQL',
        'user': 'postgres',
        'port': ''
    }
    DEBUG = True
    SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
    SQLALCHEMY_DATABASE_URI = f"postgresql://" \
                                            f"{db_info['user']}:" \
                                            f"{db_info['psw']}@" \
                                            f"{db_info['host']}/" \
                                            f"{db_info['database']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
