from flask import Flask, url_for
app = Flask(__name__)

# The homepage of the application
@app.route("/")
def webroot():
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
