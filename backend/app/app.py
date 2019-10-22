from flask import Flask

from .config import BaseConfig


def make_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    from .services.mongo import mongo
    mongo.init_app(app)

    from .blueprints import api, entrypoint
    app.register_blueprint(api.blueprint)
    app.register_blueprint(entrypoint.blueprint)
    return app
