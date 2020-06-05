"""configurations for Flask"""
from environs import Env

env = Env()
env.read_env()


class Config(object):
    """config object passed to flask on create_app"""

    SECRET_KEY = env.str("FLASK_SECRET_KEY")
