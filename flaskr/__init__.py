from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importer et enregistrer les blueprints
    from . import hello
    app.register_blueprint(hello.bp)

    return app
