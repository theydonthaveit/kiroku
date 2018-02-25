import os


class Config(object):

    ALEMBIC_CONTEXT = {
        'render_as_batch': True
    }


class Dev(Config):

    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://alan:kiroku@postgres:5432/kiroku'
    SQLALCHEMY_DATABASE_URI = 'postgresql://orajzfxrmovnsa:5b924f7d92c7faa14a0eafc35d9b05af4f62981f66583757a53513162f8a9081@ec2-54-247-101-191.eu-west-1.compute.amazonaws.com:5432/dsnmc7ts3e869'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_USERNAME = 'admin'
    BASIC_AUTH_PASSWORD = 'secret'


settings = globals()[os.environ.get('FLASK_CONFIG', 'Dev')]
