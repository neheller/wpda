from pathlib import Path
import shutil
from flask import Flask, url_for
import os

from .config import config

package_dir = str(Path(__file__).resolve().parent)

# App factory
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # app.config.from_pyfile('app.cfg', silent=True)
        config(app)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
    from wpda.auth import login_required

    # The homepage of the application
    @app.route("/")
    @login_required
    def index():
        return "Hello, world!"

    # Handling project list and project pages
    @app.route("/projects/<project>")
    def projects(project):
        #TODO
        return "Welcome to project %s!" % project

    # Allow get request to /projects without the trailing slash
    @app.route("/projects/")
    def project_not_specified():
        #TODO
        return projects("")

    # Generic call to annotate
    @app.route("/annotate/<project>/<dat>")
    def annotate(project, dat):
        #TODO
        return "%s - %s" % (project, dat)
    # Allow get request to /annotate/<project> without the trailing slash
    # this is used for getting list of things to annotate
    @app.route("/annotate/<project>/")
    def annotate_dat_not_specified(project):
        #TODO
        return annotate(project, "")

    # See annotation instructions
    @app.route("/instructions/<project>")
    def instructions(project):
        #TODO
        return "instructions for %s here" % project

    # See bug reporting instructions
    @app.route("/bugs/")
    def bugs():
        #TODO
        return "report a bug"


    return app
