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
)

from pymntos_web.config import Config


def create_app():
    """Create Flask app.

    """
    app = Flask(__name__, static_url_path="/static")
    app.config.from_object(Config)

    with app.app_context():
        initialize_extensions(app)
        register_blueprints(app)

    @app.route("/", methods=["POST", "GET"])
    def root():
        return render_template("index.html", title="pymntos")

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html", title="404")

    return app


def initialize_extensions(app):
    """Initialize app extensions here"""


def register_blueprints(app):
    """Set up blueprints for routing"""

    # from pymntos_web.main.views import main_blueprint

    # app.register_blueprint(main_blueprint, url_prefix="/main")
