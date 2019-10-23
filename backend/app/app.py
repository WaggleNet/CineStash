from flask import Flask
from bson import ObjectId
import json

from .config import BaseConfig


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def make_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    from .services.mongo import mongo
    mongo.init_app(app)
    app.json_encoder = JSONEncoder

    from .blueprints import api, entrypoint
    app.register_blueprint(api.blueprint)
    app.register_blueprint(entrypoint.blueprint)
    return app
