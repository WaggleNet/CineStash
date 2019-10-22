from os import environ


class BaseConfig:
    DEBUG = True if environ.get('DEBUG') else False
    TESTING = True if environ.get('TESTING') else False

    MONGO_URI = environ.get('MONGO_URI', 'mongodb://localhost/cinestash')
    SECRET_KEY = environ.get('SECRET_KEY', '123321123321')
