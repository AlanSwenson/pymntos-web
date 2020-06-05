"""configurations for Flask"""
import os
from environs import Env

env = Env()
env.read_env()


class Config(object):
    """config object passed to flask on create_app"""

    SECRET_KEY = env.str("FLASK_SECRET_KEY")
    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, "dist")
