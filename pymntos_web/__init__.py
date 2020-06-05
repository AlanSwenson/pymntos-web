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
    send_from_directory,
)

from pymntos_web.config import Config


def create_app():
    """Create Flask app.

    """
    app = Flask(__name__, static_folder="static", template_folder="./dist/")
    app.config.from_object(Config)

    with app.app_context():
        initialize_extensions(app)
        register_blueprints(app)

    @app.route("/")
    def index_client():
        dist_dir = current_app.config["DIST_DIR"]
        entry = os.path.join(dist_dir, "index.html")
        return send_file(entry)

    @app.route("/js/<path:path>")
    def send_js(path):
        dist_dir = current_app.config["DIST_DIR"]
        js_dir = os.path.join(dist_dir, "js/")
        entry = os.path.join(js_dir, path)
        return send_file(entry)

    @app.route("/css/<path:path>")
    def send_css(path):
        dist_dir = current_app.config["DIST_DIR"]
        css_dir = os.path.join(dist_dir, "css/")
        entry = os.path.join(css_dir, path)
        return send_file(entry)

    @app.route("/fonts/<path:path>")
    def send_fonts(path):
        dist_dir = current_app.config["DIST_DIR"]
        fonts_dir = os.path.join(dist_dir, "fonts/")
        entry = os.path.join(fonts_dir, path)
        return send_file(entry)

    @app.route("/img/<path:path>")
    def send_img(path):
        dist_dir = current_app.config["DIST_DIR"]
        img_dir = os.path.join(dist_dir, "img/")
        entry = os.path.join(img_dir, path)
        return send_file(entry)

    @app.route("/service-worker.js")
    def send_sw():
        dist_dir = current_app.config["DIST_DIR"]
        entry = os.path.join(dist_dir, "service-worker.js")
        return send_file(entry)

    return app


def initialize_extensions(app):
    """Initialize app extensions here"""


def register_blueprints(app):
    """Set up blueprints for routing"""

    # from pymntos_web.main.views import main_blueprint

    # app.register_blueprint(main_blueprint, url_prefix="/main")
