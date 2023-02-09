import os
from datetime import datetime

from flask import Flask
from flask_jsglue import JSGlue
from pony.flask import Pony

from flask_heroku_template.blueprint_template.api import blueprint_template_api_bp
from flask_heroku_template.blueprint_template.page import blueprint_template_page_bp
from flask_heroku_template.utils import CustomJSONEncoder

os.environ["DATETIME_STR_FORMAT"] = "%Y-%m-%d %H:%M:%S.%f"
os.environ["RUN_TIME"] = datetime.now().strftime(os.getenv("DATETIME_STR_FORMAT"))


def initialize_flask() -> Flask:
    flask_app = Flask(
        __name__, instance_relative_config=True,
        template_folder='utils/templates', static_folder='utils/static', static_url_path='/assets'
    )
    flask_app.secret_key = os.getenv("SECRET_KEY")
    flask_app.json_encoder = CustomJSONEncoder
    return flask_app


def initialize_database(flask_app):
    return Pony(flask_app)


def initialize_flask_js_glue(flask_app):
    return JSGlue(flask_app)


def register_blueprints(flask_app):
    flask_app.register_blueprint(blueprint_template_api_bp, url_prefix="/api/blueprint_template")
    flask_app.register_blueprint(blueprint_template_page_bp, url_prefix="/blueprint_template")


def jinja2_integration(flask_app):
    # flask_app.jinja_env.globals.update(isinstance=isinstance)
    pass


def create_app() -> Flask:
    flask_app = initialize_flask()
    initialize_database(flask_app)
    initialize_flask_js_glue(flask_app)
    jinja2_integration(flask_app)
    register_blueprints(flask_app)
    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
