from flask_pymongo import PyMongo

mongo = PyMongo()


def project_db():
    return mongo.db.projects
