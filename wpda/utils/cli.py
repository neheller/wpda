import subprocess
import os

import wpda

"""The command line interface to wpda"""

# Start server
def serve():
    # Set environment variable to server file location
    os.environ["FLASK_APP"] = wpda.server_file

    # Run flask server
    run_command = "flask run"
    try:
        _ = subprocess.check_call(run_command.split())
    except:
        # Probably a keyboard interrupt. Print a line because it looks nice
        print()
