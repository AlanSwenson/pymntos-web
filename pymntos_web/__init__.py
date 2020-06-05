import os

from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    Response,
    session,
    current_app,
    request,
    jsonify,
    abort,
    flash,
    send_file,
)

from pymntos_web.config import Config


def create_app():
    """Create Flask app.

    """
    app = Flask(__name__, static_folder="./dist/")
    app.config.from_object(Config)

    with app.app_context():
        initialize_extensions(app)
        register_blueprints(app)

    @app.route("/")
    def index_client():
        dist_dir = current_app.config["DIST_DIR"]
        entry = os.path.join(dist_dir, "index.html")
        return send_file(entry)

    return app


def initialize_extensions(app):
    """Initialize app extensions here"""


def register_blueprints(app):
    """Set up blueprints for routing"""

    # from pymntos_web.main.views import main_blueprint

    # app.register_blueprint(main_blueprint, url_prefix="/main")
