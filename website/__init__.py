from flask import Flask

def create_webapp(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    

    from .home.home import homeBP
    from .settings.settings import settingsBP

    app.register_blueprint(homeBP)
    app.register_blueprint(settingsBP)

    return app