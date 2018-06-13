from pathlib import Path
import socket
import sys

""" Configuration information for running server instance """

hostname = socket.gethostname()
webroot = Path(sys.argv[0]).parent.resolve()

if __name__ == '__main__':
    print("hostname", hostname)
    print("webroot:", str(webroot))
