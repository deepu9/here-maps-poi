import os
from flask import Flask


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        # load config
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load from test_config
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import index
    app.register_blueprint(index.bp)
    app.add_url_rule('/', endpoint='index')

    from . import restaurants
    app.register_blueprint(restaurants.bp)

    return app
