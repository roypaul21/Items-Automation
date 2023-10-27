from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_webapp(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        MYSQL_HOST="localhost",
        MYSQL_DB="itemschema",  
        MYSQL_USER="root",
        MYSQL_PASSWORD="Izakme!@#4",
    )

    mysql.init_app(app)

    from .home.home import homeBP
    from .settings.settings import settingsBP

    app.register_blueprint(homeBP)
    app.register_blueprint(settingsBP)

    return app
