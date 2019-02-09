def configure_app():
    import os
    import dotenv
    import flask
    PROJECT_ROOT = os.path.dirname(__file__)
    dotenv.load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, '.env'))
    app = flask.Flask(__name__)
    return app


app = configure_app()
