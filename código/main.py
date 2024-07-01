from app import routes
from flask import Flask

app = Flask(__name__)

def create_app():
    app.register_blueprint(routes.bp)

    return app

app = create_app()
